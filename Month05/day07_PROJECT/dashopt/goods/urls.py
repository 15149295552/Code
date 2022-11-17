from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    # 首页展示: v1/goods/index
    path("index", cache_page(300, cache="index")(views.GoodsIndexView.as_view())),
    # 详情页展示: v1/goods/detail/sku_id
    path("detail/<int:sku_id>", views.GoodsDetailView.as_view()),
]










