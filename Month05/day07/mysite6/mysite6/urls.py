"""mysite6 URL Configuration

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
from django.urls import path
from django.views.decorators.cache import cache_page

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # 设置cookie：登录
    path("set_cookie/", views.set_cookie_view),
    # 获取cookie：查看订单
    path("get_cookie/", views.get_cookie_view),
    # 设置session
    path("set_session/", views.set_session_view),
    # 获取session
    path("get_session/", views.get_session_view),
    # 缓存cache
    path("test_cache/", cache_page(30)(views.test_cache_view)),
    # 中间件测试
    path("test", views.test_view),
    # 发送邮件
    path("email", views.email_view),
]
