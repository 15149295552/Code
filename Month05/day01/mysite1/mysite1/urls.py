"""mysite1 URL Configuration

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000
    path("", views.index_view),
    # # http://127.0.0.1:8000/page/1
    # path("page/1", views.page1_view),
    # # http://127.0.0.1:8000/page/2
    # path("page/2", views.page2_view),
    # path转换器
    # http://127.0.0.1:8000/page/666
    # page_num = 666
    path("page/<int:page_num>", views.page_view),
    # 计算器: 8000/整数/操作/整数
    path("<int:x>/<str:operation>/<int:y>", views.cal_view),
    # 登录功能:v1/users/login
    path("v1/users/login", views.login_view),
]
