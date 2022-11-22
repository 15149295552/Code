"""dashopt URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # 用户模块: v1/users/
    path('v1/users/', include('users.urls')),
    # 商品模块: v1/goods/
    path('v1/goods/', include('goods.urls')),
    # 购物车模块: v1/carts/
    path('v1/carts/', include('carts.urls')),
    # 订单模块: v1/orders/
    path('v1/orders/', include('orders.urls')),
    # 支付模块: v1/pays/
    path('v1/pays/', include('pays.urls')),
]

# 配置静态路由
# http://127.0.0.1:8000/media/sku/1.png
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

