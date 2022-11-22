import time
from alipay import AliPay

from django.conf import settings
from django.core.cache import caches
from django.http import JsonResponse
from django.db import transaction
from django.views import View

from carts.views import CartsView
from goods.models import SKU
from orders.models import OrderInfo, OrderGoods
from users.models import Address
from utils.logging_dec import logging_check


class AdvanceView(View):
    @logging_check
    def get(self, request, username):
        """
        确认订单页视图逻辑
        1.购物车链条: settlement_type=0
        2.立即购买链条
          settlement_type=1&sku_id=2&buy_num=5
        """
        data = request.GET
        settle = data.get("settlement_type")
        if settle not in ["0", "1"]:
            return JsonResponse({"code": 10400, "error": "非法请求!"})

        buy_num = 0
        sku_id = 0

        # 上半部分:收货地址信息
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

        # 下半部分:订单商品信息
        if settle == "0":
            # 购物车
            # {"1":[8,1], "2":[5,0]}
            carts_dict = CartsView().get_carts_dict(user.id)
            selected_dict = {k: v for k, v in carts_dict.items() if v[1] == 1}
            sku_list = CartsView().get_sku_list(selected_dict)
        else:
            # 立即购买
            sku_id = data.get("sku_id")
            buy_num = data.get("buy_num")
            buy_num = int(buy_num)
            # 组装carts_dict:{"1":[8,1]}
            carts_dict = {sku_id: [buy_num, 1]}

            sku_list = CartsView().get_sku_list(carts_dict)

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


class OrderInfoView(View):
    @logging_check
    def post(self, request, username):
        """
        生成订单视图逻辑
        1.获取请求体数据
        2.ORM操作
          订单表中插入数据
          更新sku库存和销量
          订单商品表中插入数据
        3.返回响应
        """
        data = request.mydata
        user = request.myuser

        addr_id = data.get("address_id")
        settle = data.get("settlement_type")

        if settle not in ["0", "1"]:
            return JsonResponse({"code": 10401, "error": "违法请求"})

        # 20221121113838666
        order_id = time.strftime("%Y%m%d%H%M%S") + str(user.id)
        total_amount = 0
        total_count = 0

        # 收货地址
        try:
            addr = Address.objects.get(id=addr_id, is_delete=False)
        except Exception as e:
            return JsonResponse({"code": 10402, "error":" 请检查收货地址~"})

        # 开启事务
        with transaction.atomic():
            sid = transaction.savepoint()
            # 1.订单表中插入数据
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
                tag=addr.tag,
            )
            carts_dict = CartsView().get_carts_dict(user.id)
            if settle == "0":
                # 购物车链条
                # {"1":[8,1], "2":[5,1]}
                selected_dict = {k: v for k, v in carts_dict.items() if v[1] == 1}
                skus = SKU.objects.filter(id__in=selected_dict)

                for sku in skus:
                    count = selected_dict[str(sku.id)][0]
                    # 校验库存
                    if count > sku.stock:
                        # 回滚 + 返回
                        transaction.savepoint_rollback(sid)
                        return JsonResponse({"code": 10404, "error": f"{sku.name}库存不足,仅剩{sku.stock}件"})

                    # 2.更新SKU库存和销量
                    sku.stock -= count
                    sku.sales += count
                    sku.save()

                    # 3.订单商品表中插入数据
                    OrderGoods.objects.create(
                        order_info_id=order_id,
                        sku_id=sku.id,
                        count=count,
                        price=sku.price,
                    )

                    total_amount += sku.price * count
                    total_count += count
            else:
                # 立即购买链条
                buy_count = data.get("buy_count")
                sku_id = data.get("sku_id")
                try:
                    sku = SKU.objects.get(id=int(sku_id), is_launched=True)
                except Exception as e:
                    # 回滚 + 返回
                    transaction.savepoint_rollback(sid)
                    return JsonResponse({"code": 10405, "error": "该商品已下架"})

                # 校验库存
                buy_count = int(buy_count)
                if buy_count > sku.stock:
                    transaction.savepoint_rollback(sid)
                    return JsonResponse({"code": 10406, "error": f"该商品库存不足,仅剩{sku.stock}件~"})

                # 更新库存和销量
                sku.stock -= buy_count
                sku.sales += buy_count
                sku.save()

                # 订单商品表中插入数据
                OrderGoods.objects.create(
                    order_info_id=order_id,
                    sku_id=sku.id,
                    count=buy_count,
                    price=sku.price
                )

                total_amount = sku.price * buy_count
                total_count = buy_count

            # 更新订单总金额和总数量
            order.total_amount = total_amount
            order.total_count = total_count
            order.save()
            # 提交事务
            transaction.savepoint_commit(sid)

        if settle == "0":
            # 删除购物车中选中的商品
            unselected_dict = {k: v for k, v in carts_dict.items() if v[1] == 0}
            key = f"carts_{user.id}"
            caches["carts"].set(key, unselected_dict)
            carts_count = len(unselected_dict)
        else:
            # 立即购买链条
            carts_count = len(carts_dict)

        # 返回响应
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

    @logging_check
    def get(self, request, username):
        """
        查询订单视图逻辑
        0 - 所有订单
        1 - 待付款
        2 - 待发货
        3 - 待收货
        4 - 已完成
        5 - 去付款
        """
        status = request.GET.get("type")
        if status not in [str(i) for i in range(6)]:
            return JsonResponse({"code": 10406, "error": "违法请求"})

        user = request.myuser
        status = int(status)
        if status == 0:
            # 所有订单
            order_query = OrderInfo.objects.filter(user_profile=user)
        elif status == 5:
            # 去付款:type=5&order_id=202211211727266
            order_id = request.GET.get("order_id")
            try:
                order = OrderInfo.objects.get(order_id=order_id)
            except Exception as e:
                return JsonResponse({"code": 10407, "error": "该订单不存在~"})

            carts_count = len(CartsView().get_carts_dict(user.id))

            # 返回响应
            result = {
                "code": 200,
                "data": {
                    'saller': '达达商城',
                    'total_amount': order.total_amount,
                    'order_id': order_id,
                    'pay_url': '第三方支付路由',
                    'carts_count': carts_count
                }
            }

            return JsonResponse(result)
        else:
            # 待付款、待发货、待收货、已完成
            order_query = OrderInfo.objects.filter(user_profile=user, status=status)

        orders_list = []
        for order in order_query:
            # 一个订单中的所有商品的列表[{},{}...]
            sku_list = []
            goods_query = OrderGoods.objects.filter(order_info=order)
            for goods in goods_query:
                sku = goods.sku
                val_query = sku.sale_attr_value.all()
                goods_dict = {
                    "id": sku.id,
                    "default_image_url": str(sku.default_image_url),
                    "name": sku.name,
                    "price": goods.price,
                    "count": goods.count,
                    "total_amount": goods.price * goods.count,
                    "sku_sale_attr_names": [i.spu_sale_attr.name for i in val_query],
                    "sku_sale_attr_vals": [i.name for i in val_query]
                }
                sku_list.append(goods_dict)

            # 返回数据的大字典
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

    @logging_check
    def put(self, request, username):
        """
        确认收货视图逻辑
        1.获取请求体数据(order_id)
        2.一查二改三保存(status 3-->4)
        3.返回响应 {"code":200}
        """
        order_id = request.mydata.get("order_id")
        try:
            order = OrderInfo.objects.get(order_id=order_id)
        except Exception as e:
            return JsonResponse({"code": 10409, "error": "操作失败,请重试~"})

        order.status = 4
        order.save()

        return JsonResponse({"code": 200})

    def get_pay_url(self, order_id, total_amount):
        """
        功能函数:生成第三方支付的路由
        """
        # 1.创建对象
        alipay = AliPay(
            # 应用ID:控制台获取
            appid=settings.ALIPAY_APPID,
            # 异步通知地址[POST请求]:必须为公网IP
            app_notify_url=None,
            # 应用私钥:用于签名
            app_private_key_string=open(settings.ALIPAY_KEYS_DIR + "app_private_key.pem").read(),
            # 支付宝公钥:用于验签
            alipay_public_key_string=open(settings.ALIPAY_KEYS_DIR + "alipay_public_key.pem").read(),
            # 签名使用算法
            sign_type="RSA2",
            # True:请求发至沙箱,False:生产环境
            debug=True
        )
        # 2.调用方法生成支付路由
        params = alipay.api_alipay_trade_page_pay(
            # 订单标题
            subject=order_id,
            # 订单编号
            out_trade_no=order_id,
            # 订单总金额
            total_amount=total_amount,
            # 同步通知地址
            return_url=settings.ALIPAY_RETURN_URL,
            # 异步通知地址
            notify_url=settings.ALIPAY_NOTIFY_URL,
        )

        return "https://openapi.alipaydev.com/gateway.do?" + params


