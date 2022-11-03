from django.contrib import admin
from orders.models import UserProfile, OrderInfo, OrderGoods


admin.site.register(UserProfile)
admin.site.register(OrderInfo)
admin.site.register(OrderGoods)
