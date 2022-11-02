from django.urls import path
from . import views


urlpatterns = [
    # 注册功能:v1/users/register
    path("register", views.register_view),
    # 登录功能:v1/users/login
    path("login", views.login_get_view),
    # 修改密码:v1/users/update_password
    path("update_password", views.update_view),
    # 注销用户:v1/users/delete_user
    path("delete_user", views.delete_view),
]














