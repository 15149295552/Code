from django.urls import path
from . import views

# 文章信息
urlpatterns = [
    path('topics/<str:author_id>',views.TopicViews.as_view())
]

# 留言信息
urlpatterns += [

]