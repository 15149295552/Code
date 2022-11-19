from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserViews.as_view()),
    path('<str:username>', views.UserViews.as_view()),
    path('<str:username>/avatar', views.users_views),
    path('<str:username>/password', views.change_password),
    #v1/users/sms
    # path('sms', views.sms_view),

]