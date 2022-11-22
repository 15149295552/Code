from django.urls import path
from . import views


urlpatterns = [
    # 注册: v1/users/register
    path("register", views.register_view),
    # 登录: v1/users/login
    path("login", views.login_view),
    # 邮件激活: v1/users/activation
    path("activation", views.active_view),
    # 地址管理[新增和查询]: v1/users/username/address
    path("<str:username>/address", views.AddressView.as_view()),
    # 地址管理[修改和删除]: v1/users/username/address/id
    path("<str:username>/address/<int:id>", views.AddressView.as_view()),
    # 地址管理[默认地址]: v1/users/username/address/default
    path("<str:username>/address/default", views.DefaultAddressView.as_view()),
    # 短信验证码: v1/users/sms/code
    path("sms/code", views.sms_view),
    # 微博登录[授权码]: v1/users/weibo/authorization
    path("weibo/authorization", views.OAuthWeiBoCodeView.as_view()),
    # 微博登录[访问令牌]: v1/users/weibo/users
    path("weibo/users", views.OAuthWeiBoTokenView.as_view()),
    # 有用户立即绑定: v1/users/weibo/users/binduser
    path("weibo/users/binduser", views.BindUserView.as_view()),
]



