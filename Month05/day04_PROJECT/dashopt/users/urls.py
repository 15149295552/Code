from django.urls import path
from . import views


urlpatterns = [
    # 注册: v1/users/register
    path("register", views.register_view),
    # 登录: v1/users/login
    path("login", views.login_view),
    # 邮件激活: v1/users/activation
    path("activation", views.active_view),
    # 地址管理[新增和查询]: v1/users/username/address
    path("<str:username>/address", views.AddressView.as_view()),
    # 地址管理[修改和删除]: v1/users/username/address/id
    path("<str:username>/address/<int:id>", views.AddressView.as_view()),
    # 地址管理[默认地址]: v1/users/username/address/default
    path("<str:username>/address/default", views.DefaultAddressView.as_view()),
    # 短信验证码: v1/users/sms/code
    path("sms/code", views.sms_view),
]



