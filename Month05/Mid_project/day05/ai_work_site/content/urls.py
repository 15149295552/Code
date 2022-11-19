from django.urls import path
from . import views

# 文章处理，留言处理，
urlpatterns = [
    path('topics/<str:author_id>', views.TopicViews.as_view()),
    path('messages/<int:topic_id>', views.message_view),
    # path('student/<int:month>', views.student_view),
    # path('work/<int:month>', views.work_view)

]

