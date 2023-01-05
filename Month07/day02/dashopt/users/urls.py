from django.urls import path
from . import views

urlpatterns = [
    # 注册功能: v1/users/register
    path("register", views.register_view),
    # 登录功能: v1/users/login
    path("login", views.login_view),
    # 地址管理: v1/users/<username>/address
    path("<str:username>/address", views.AddressView.as_view()),
]











