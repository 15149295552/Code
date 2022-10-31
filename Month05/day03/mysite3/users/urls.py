from django.urls import path
from . import views


urlpatterns = [
    # 注册功能:v1/users/register
    path("register", views.register_view),
]














