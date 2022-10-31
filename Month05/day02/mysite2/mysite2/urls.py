"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("birthday", views.birth_view),
    # 首页
    path("", views.index_view),
    # 用户模块:
    # path("v1/users/", include("users.urls"))

    # 登录:v1/users/login
    # 注册:v1/users/register
    # 第三方登录:v1/users/qqlogin
    # 修改密码:v1/users/update_password
    # 找回密码:v1/users/find_password
    # 订单模块:
    # 查询订单:v1/orders/get_orders
    # 体育应用
    path("v1/sports/", include("sports.urls")),
    # nba应用
    path("v1/nba/", include("nba.urls")),
]
