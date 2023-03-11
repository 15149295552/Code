# wdb add
from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    # path('', views.index),
    # # 添加带有字符类型、整型的slug的URL
    # path("<year>/<int:month>/<slug:day>", views.mydate),
    # re_path("(?P<year>[0-9]{4}).html", views.myyear, name="myyear"), # 将URL命名为myyear
    # # 设置name和month参数(参数值为05)
    # re_path("dict/(?P<year>[0-9]{4}).html", views.myyear_dict, {"month":"05"}, name="myyear_dict"),
    path("do_infer.html", views.do_infer),
]
