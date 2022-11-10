from django.urls import path
from . import views


urlpatterns = [
    # 注册: v1/users/register
    path("register", views.register_view),
    # 登录: v1/users/login
    path("login", views.login_view),
    # 邮件激活: v1/users/activation
    path("activation", views.active_view),
]



