from django.conf import settings
from django.views import View
from django.http import JsonResponse
from django.core.cache import caches

from goods.models import SKU
from utils.logging_dec import logging_check


class CartsView(View):
    @logging_check
    def post(self, request, username):
        """
        添加购物车视图逻辑
        1.获取请求体数据
        2.存入Redis数据库
          carts_1: {"1":[5,1],"2":[8,0]}
        3.返回响应
        """
        # 1.请求体数据
        data = request.mydata
        sku_id = data.get("sku_id")
        count = int(data.get("count"))

        # 校验上下架状态和库存
        try:
            sku = SKU.objects.get(id=int(sku_id), is_launched=True)
        except Exception as e:
            return JsonResponse({"code": 10300, "error": "该商品已下架"})

        if count > sku.stock:
            return JsonResponse({"code": 10301, "error": f"库存不足,仅剩{sku.stock}件"})

        # 2.获取该用户购物车数据
        user_id = request.myuser.id
        # carts_dict: {"1":[8,1],"2":[5,0]}
        carts_dict = self.get_carts_dict(user_id)

        # {"1": [8, 1], "2": [5, 0]}
        if sku_id in carts_dict:
            carts_dict[sku_id][0] += count
        else:
            carts_dict[sku_id] = [count, 1]

        # 更新到redis
        key = f"carts_{user_id}"
        caches["carts"].set(key, carts_dict)

        # 返回响应
        result = {
            'code': 200,
            'data': {
                'carts_count': len(carts_dict)
            },
            'base_url': settings.PIC_URL
        }

        return JsonResponse(result)

    @logging_check
    def get(self, request, username):
        """
        查询购物车视图逻辑
        1.先从Redis获取数据
        2.再从MySQL获取数据
        3.返回响应
          {"code":200,"data":[],...}
        """
        user = request.myuser
        # {"1":[8,1],"2":[5,0]}
        carts_dict = self.get_carts_dict(user.id)
        data = self.get_sku_list(carts_dict)

        result = {
            "code": 200,
            "data": data,
            "base_url": settings.PIC_URL
        }

        return JsonResponse(result)

    @logging_check
    def delete(self, request, username):
        """
        删除购物车视图逻辑
        1.获取请求体数据
        2.删除数据(Redis)
          {"1":[8,1], "2":[6,1]}
        3.返回响应
        """
        data = request.mydata
        sku_id = data.get("sku_id")

        user = request.myuser
        # {"1":[8,1], "2":[6,1]}
        carts_dict = self.get_carts_dict(user.id)

        if str(sku_id) not in carts_dict:
            return JsonResponse({"code": 10303, "error": "无此商品"})

        carts_dict.pop(str(sku_id))

        # 更新到Redis
        caches["carts"].set(f"carts_{user.id}", carts_dict)

        # 返回响应
        result = {
            "code": 200,
            "data": {"carts_count": len(carts_dict)},
            "base_url": settings.PIC_URL
        }

        return JsonResponse(result)

    @logging_check
    def put(self, request, username):
        """
        修改购物车视图逻辑
        1.获取请求体数据
        2.修改Redis数据
        3.返回响应
        """
        data = request.mydata
        user = request.myuser

        sku_id = data.get("sku_id")
        state = data.get("state")

        carts_dict = self.get_carts_dict(user.id)

        # {"1":[8,0], "2":[5,0]}
        if state == "add":
            carts_dict[sku_id][0] += 1
        elif state == "del":
            count = carts_dict[sku_id][0]
            if count == 1:
                return JsonResponse({"code": 10305, "error": "商品数量不能为0"})
            else:
                carts_dict[sku_id][0] -= 1
        elif state == "select":
            carts_dict[sku_id][1] = 1
        elif state == "unselect":
            carts_dict[sku_id][1] = 0
        elif state == "selectall":
            # {"1":[8,1], "2":[5,0]}
            for k in carts_dict:
                carts_dict[k][1] = 1
        elif state == "unselectall":
            for k in carts_dict:
                carts_dict[k][1] = 0
        else:
            return JsonResponse({"code": 10304, "error": "违法请求"})

        # 更新到Redis
        caches["carts"].set(f"carts_{user.id}", carts_dict)
        data = self.get_sku_list(carts_dict)
        result = {
            "code": 200,
            "data": data,
            "base_url": settings.PIC_URL
        }

        return JsonResponse(result)

    def get_carts_dict(self, user_id):
        """
        功能函数:获取购物车数据
        carts_1: {"1":[5,1],"2":[8,0]}
        """
        key = f"carts_{user_id}"
        data = caches["carts"].get(key)
        if not data:
            return {}

        return data

    def get_sku_list(self, carts_dict):
        """
        功能函数:获取购物车数据
        """
        data = []
        # {"1":[8,1],"2":[5,0]}
        for sku_id in carts_dict:
            try:
                sku = SKU.objects.get(id=int(sku_id))
            except Exception as e:
                continue

            value_query = sku.sale_attr_value.all()
            sku_dict = {
                "id": sku.id,
                "name": sku.name,
                # {"1":[8,1],"2":[5,0]}
                "count": carts_dict[sku_id][0],
                "selected": carts_dict[sku_id][1],
                "default_image_url": str(sku.default_image_url),
                "price": sku.price,
                "sku_sale_attr_name": [i.spu_sale_attr.name for i in value_query],
                "sku_sale_attr_val": [i.name for i in value_query]
            }
            data.append(sku_dict)

        return data









