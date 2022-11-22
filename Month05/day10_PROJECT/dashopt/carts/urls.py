from django.urls import path
from . import views


urlpatterns = [
    # 购物车: v1/carts/<username>
    path("<str:username>", views.CartsView.as_view()),
]












