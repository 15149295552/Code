import time
from alipay import AliPay

from django.conf import settings
from django.core.cache import caches
from django.db import transaction
from django.http import JsonResponse

from carts.views import CartsView
from goods.models import SKU
from orders.models import OrderInfo, OrderGoods
from users.models import Address
from utils.baseview import BaseView


class AdvanceView(BaseView):
    def get(self, request, username):
        """
        订单确认页视图逻辑
        来源:
        1.购物车: settlement_type=0
        2.立即购买:settlement_type=1&sku_id=1&buy_num=3
        响应
        """
        buy_num = 0
        sku_id = 0
        # 1.获取收货地址
        addresses = []
        user = request.myuser
        addr_query = Address.objects.filter(user_profile=user, is_delete=False)
        for addr in addr_query:
            addr_dict = {
                "id": addr.id,
                "name": addr.receiver,
                "mobile": addr.receiver_mobile,
                "title": addr.tag,
                "address": addr.address
            }
            if addr.is_default:
                addresses.insert(0, addr_dict)
            else:
                addresses.append(addr_dict)

        # 2.获取商品信息
        settle = request.GET.get("settlement_type")
        if settle not in ["0", "1"]:
            return JsonResponse({"code": 10400, "error": "违法请求！"})

        if settle == "0":
            # 购物车链条
            key = f"carts_{user.id}"
            # {"1":[8,1], "2":[5,0],"3":[4,1]}
            carts_dict = caches["carts"].get(key)
            dic1 = {k: v for k, v in carts_dict.items() if v[1] == 1}
            sku_list = CartsView().get_skus_list(dic1)
        else:
            # 立即购买链条
            sku_id = request.GET.get("sku_id")
            buy_num = request.GET.get("buy_num")
            buy_num = int(buy_num)
            # 校验库存
            try:
                sku = SKU.objects.get(id=int(sku_id), is_launched=True)
            except Exception as e:
                return JsonResponse({"code": 10401, "error": "该商已下架!"})

            if buy_num > sku.stock:
                return JsonResponse({"code": 200, "error": f"库存不足,仅剩{sku.stock}件"})

            # 组织列表
            value_query = sku.sale_attr_value.all()
            sku_list = [
                {
                    "id": sku.id,
                    "name": sku.name,
                    "count": buy_num,
                    "selected": 1,
                    "default_image_url": str(sku.default_image_url),
                    "price": sku.price,
                    "sku_sale_attr_name": [i.spu_sale_attr.name for i in value_query],
                    "sku_sale_attr_val": [i.name for i in value_query]
                }
            ]

        result = {
            "code": 200,
            "data": {
                "addresses": addresses,
                "sku_list": sku_list,
                "buy_count": buy_num,
                "sku_id": sku_id
            },
            "base_url": settings.PIC_URL
        }

        return JsonResponse(result)


class OrderView(BaseView):
    def post(self, request, username):
        """
        生成订单视图逻辑
        1.获取请求体数据
        2.3个ORM操作
        3.返回响应
        """
        data = request.mydata
        settle = data.get("settlement_type")

        if settle not in ["0", "1"]:
            return JsonResponse({"code": 10403, "error": "违法请求!"})

        user = request.myuser
        order_id = time.strftime("%Y%m%d%H%M%S") + str(user.id)
        total_amount = 0
        total_count = 0

        address_id = data.get("address_id")
        try:
            addr = Address.objects.get(id=address_id, is_delete=False)
        except Exception as e:
            return JsonResponse({"code": 10404, "error": "地址异常!"})

        # 开启事务
        with transaction.atomic():
            sid = transaction.savepoint()
            order = OrderInfo.objects.create(
                user_profile=user,
                order_id=order_id,
                total_amount=total_amount,
                total_count=total_count,
                pay_method=1,
                freight=0,
                status=1,
                receiver=addr.receiver,
                address=addr.address,
                receiver_mobile=addr.receiver_mobile,
                tag=addr.tag
            )
            # 更新库存和销量
            # {"1":[5,1], "2":[8,1], "3":[4,0]}
            carts_dict = CartsView().get_carts_dict(user.id)
            if settle == "0":
                # {"1":[5,1], "2":[8,1]}
                dic1 = {k: v for k, v in carts_dict.items() if v[1] == 1}
                for sku_id in dic1:
                    # 校验库存 上下架状态
                    try:
                        sku = SKU.objects.get(id=int(sku_id), is_launched=True)
                    except Exception as e:
                        # 回滚 + 返回
                        transaction.savepoint_rollback(sid)
                        return JsonResponse({"code": 10405, "error": f"{sku.name}已下架"})

                    count = dic1[sku_id][0]
                    if sku.stock < count:
                        transaction.savepoint_rollback(sid)
                        return JsonResponse({"code": 10406, "error": f"{sku.name}库存不足,仅剩{sku.stock}件"})

                    # 更新库存和销量(一查二改三保存)
                    sku.stock -= count
                    sku.sales += count
                    sku.save()

                    # 订单商品表插入数据
                    OrderGoods.objects.create(
                        order_info=order,
                        sku=sku,
                        count=count,
                        price=sku.price
                    )

                    total_amount += sku.price * count
                    total_count += count
            else:
                # 立即购买链条
                sku_id = data.get("sku_id")
                buy_count = data.get("buy_count")
                sku_id = int(sku_id)
                buy_count = int(buy_count)
                # 上下架状态 库存
                try:
                    sku = SKU.objects.get(id=sku_id, is_launched=True)
                except Exception as e:
                    transaction.savepoint_rollback(sid)
                    return JsonResponse({"code": 10407, "error": "该商品已下架"})

                if sku.stock < buy_count:
                    transaction.savepoint_rollback(sid)
                    return JsonResponse({"code": 10408, "error": f"库存不足,仅剩{sku.stock}件"})

                sku.stock -= buy_count
                sku.sales += buy_count
                sku.save()

                OrderGoods.objects.create(
                    order_info=order,
                    sku=sku,
                    price=sku.price,
                    count=buy_count
                )

                total_amount += sku.price * buy_count
                total_count += buy_count

            # 更新总金额和总数量
            order.total_amount = total_amount
            order.total_count = total_count
            order.save()

            # 提交事务
            transaction.savepoint_commit(sid)

        if settle == "0":
            # 删除购物车中选中状态为1的商品
            dic2 = {k: v for k, v in carts_dict.items() if v[1] == 0}
            key = f"carts_{user.id}"
            caches["carts"].set(key, dic2)
            carts_count = len(dic2)
        else:
            carts_count = len(carts_dict)

        result = {
            "code": 200,
            "data": {
                'saller': '达达商城',
                'total_amount': total_amount,
                'order_id': order_id,
                'pay_url': self.get_pay_url(order_id, float(total_amount)),
                'carts_count': carts_count
            }
        }

        return JsonResponse(result)

    def get(self, request, username):
        """
        查询订单视图逻辑
            type=0 ：所有订单
            type=1 ：待付款订单
            type=2 ：待发货订单
            type=3 ：待收货订单
            type=4 ：已完成订单
            type=5 ：去付款
        """
        status = request.GET.get("type")
        if status not in [str(i) for i in range(6)]:
            return JsonResponse({"code": 10409, "error": "违法请求"})

        status = int(status)
        user = request.myuser
        if status == 0:
            # 该用户所有订单
            order_query = OrderInfo.objects.filter(user_profile=user)
        elif status == 5:
            # 去付款:?type=5&order_id=1234567890
            order_id = request.GET.get("order_id")
            try:
                order = OrderInfo.objects.get(user_profile=request.myuser, order_id=order_id)
            except Exception as e:
                return JsonResponse({"code": 10410, "error": "该订单不存在!"})

            carts_count = len(CartsView().get_carts_dict(request.myuser.id))
            result = {
                "code": 200,
                "data": {
                    'saller': '达达商城',
                    'total_amount': order.total_amount,
                    'order_id': order_id,
                    'pay_url': self.get_pay_url(order_id, float(order.total_amount)),
                    'carts_count': carts_count
                }
            }

            return JsonResponse(result)

        else:
            # 四种订单状态
            order_query = OrderInfo.objects.filter(user_profile=user, status=status)

        orders_list = []
        for order in order_query:
            # 组装该订单商品信息的列表
            sku_list = []
            goods_query = OrderGoods.objects.filter(order_info=order)
            for goods in goods_query:
                sku = goods.sku
                value_query = sku.sale_attr_value.all()
                goods_dict = {
                    "id": sku.id,
                    "default_image_url": str(sku.default_image_url),
                    "name": sku.name,
                    "price": goods.price,
                    "count": goods.count,
                    "total_amount": goods.price * goods.count,
                    "sku_sale_attr_names": [i.spu_sale_attr.name for i in value_query],
                    "sku_sale_attr_vals": [i.name for i in value_query]
                }
                sku_list.append(goods_dict)

            # 处理每个订单为字典
            order_dict = {
                "order_id": order.order_id,
                "order_total_count": order.total_count,
                "order_total_amount": order.total_amount,
                "order_freight": order.freight,
                "address": {
                    "title": order.tag,
                    "address": order.address,
                    "mobile": order.receiver_mobile,
                    "receiver": order.receiver
                },
                "status": order.status,
                "order_sku": sku_list,
                "order_time": str(order.created_time)[:19]
            }
            orders_list.append(order_dict)

        result = {
            "code": 200,
            "data": {"orders_list": orders_list},
            "base_url": settings.PIC_URL
        }

        return JsonResponse(result)

    def get_pay_url(self, order_id, total_amount):
        """
        获取第三方支付的路由
        """
        alipay = AliPay(
            appid=settings.APPID,
            app_notify_url=None,
            app_private_key_string=open(settings.KEYS_DIR + "app_private_key.pem").read(),
            alipay_public_key_string=open(settings.KEYS_DIR + "alipay_public_key.pem").read(),
            sign_type="RSA2",
            # False:请求到生产环境,True:请求发至沙箱环境
            debug=True
        )
        # 查看接口: alipay.trade.page.pay
        # 返回值: 查询字符串
        params = alipay.api_alipay_trade_page_pay(
            # 订单标题
            subject=order_id,
            # 订单编号
            out_trade_no=order_id,
            # 总金额
            total_amount=total_amount,
            # 同步通知地址GET
            return_url=settings.RETURN_URL,
            # 异步通知地址POST
            notify_url=settings.NOTIFY_URL
        )

        return "https://openapi.alipaydev.com/gateway.do?" + params





