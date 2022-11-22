from django.urls import path
from . import views


urlpatterns = [
    # 同步通知: v1/pays/return_url
    path("return_url", views.ReturnView.as_view()),
    # 异步通知: v1/pays/notify_url
    path("notify_url", views.NotifyView.as_view()),
]

















