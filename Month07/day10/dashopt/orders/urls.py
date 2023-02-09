from django.urls import path
from . import views

urlpatterns = [
    # 订单确认页:v1/orders/<username>/advance
    path("<str:username>/advance", views.AdvanceView.as_view()),
    # 生成订单:v1/orders/<username>
    path("<str:username>", views.OrderView.as_view()),
]















