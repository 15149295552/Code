import json

from django.conf import settings
from django.core.cache import caches
from django.http import JsonResponse

from goods.models import SKU
from utils.baseview import BaseView


class CartsView(BaseView):
    def post(self, request, username):
        """
        添加购物车视图逻辑
        1.获取请求体数据(sku_id  count)
        2.获取该用户购物车数据(Redis)
          "carts_1": {"1":[3,1]}
        3.判断后,存入Redis数据库
        4.返回响应
        """
        # 获取请求体数据
        data = json.loads(request.body)
        sku_id = data.get("sku_id")
        count = data.get("count")

        user = request.myuser
        carts_dict = self.get_carts_dict(user.id)
        # 想加: sku_id="1", count="2"
        if sku_id not in carts_dict:
            carts_dict[sku_id] = [int(count), 1]
        else:
            # carts_dict: {"1":[8,1]}
            carts_dict[sku_id][0] += int(count)

        # 更新到Redis
        key = f"carts_{user.id}"
        caches["carts"].set(key, carts_dict)

        result = {
            'code': 200,
            'data': {'carts_count': len(carts_dict)},
            'base_url': settings.PIC_URL
        }

        return JsonResponse(result)

    def get(self, request, username):
        """
        查询购物车视图逻辑
        1.获取redis中该用户所有数据
        2.根据redis中的sku_id再获取mysql中数据
        3.返回响应
          {"code":200,"data":[{},...],"base_url":xxx}
        """
        user = request.myuser
        # carts_dict: {'1': [3, 1], '2': [6, 1]}
        carts_dict = self.get_carts_dict(user.id)
        skus_list = []
        for sku_id in carts_dict:
            try:
                sku = SKU.objects.get(id=int(sku_id))
            except Exception as e:
                continue

            value_query = sku.sale_attr_value.all()

            sku_dict = {
                "id": sku.id,
                "name": sku.name,
                "count": carts_dict[sku_id][0],
                "selected": carts_dict[sku_id][1],
                "default_image_url": str(sku.default_image_url),
                "price": sku.price,
                "sku_sale_attr_name": [i.spu_sale_attr.name for i in value_query],
                "sku_sale_attr_val": [i.name for i in value_query]
            }
            skus_list.append(sku_dict)

        result = {
            "code": 200,
            "data": skus_list,
            "base_url": settings.PIC_URL
        }

        return JsonResponse(result)

    def delete(self, request, username):
        """
        删除购物车商品视图逻辑
        1.获取请求体数据(sku_id)
        2.获取购物车数据,再删除,再更新到Redis
        3.返回响应
        """
        user = request.myuser
        data = request.mydata
        sku_id = data.get("sku_id")

        # carts_dict: {"1":[3,1], "2":[5,0]}
        carts_dict = self.get_carts_dict(user.id)
        # 删除对应的key
        carts_dict.pop(str(sku_id))
        # 更新到redis
        key = f"carts_{user.id}"
        caches["carts"].set(key, carts_dict)

        result = {
            'code': 200,
            'data': {'carts_count': len(carts_dict)},
            'base_url': settings.PIC_URL
        }

        return JsonResponse(result)

    def put(self, request, username):
        """
        修改购物车视图逻辑
        +1操作：add  还有sku_id数据
        -1操作：del  还有sku_id数据
        单选：select  还有sku_id数据
        取消单选：unselect  还有sku_id数据
        全选：selectall
        取消全选：unselectall

        1.获取请求体数据(state、sku_id)
        2.获取该用户购物车所有数据
        3.根据state做对应的操作
        4.更新到redis
        5.返回响应
        """
        pass

    def get_carts_dict(self, user_id):
        """
        功能函数,返回购物车数据的字典
        :return {}
        """
        # "carts_1": {}
        key = f"carts_{user_id}"
        carts_dict = caches["carts"].get(key)
        if not carts_dict:
            return {}

        return carts_dict








