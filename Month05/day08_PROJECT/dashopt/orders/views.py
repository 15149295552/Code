from django.conf import settings
from django.http import JsonResponse
from django.views import View

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
            pass
        else:
            # 立即购买
            pass

        result = {
            "code": 200,
            "data": {
                "addresses": addresses,
                "sku_list": []
            },
            "base_url": settings.PIC_URL
        }

        return JsonResponse(result)


