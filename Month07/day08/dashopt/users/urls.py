from django.urls import path
from . import views

urlpatterns = [
    # 注册功能: v1/users/register
    path("register", views.register_view),
    # 登录功能: v1/users/login
    path("login", views.login_view),
    # 地址管理[新增和查询]: v1/users/<username>/address
    path("<str:username>/address", views.AddressView.as_view()),
    # 地址管理[修改和删除]: v1/users/<username>/address/<id>
    path("<str:username>/address/<int:id>", views.AddressView.as_view()),
    # 地址管理[默认地址]: v1/users/<username>/address/default
    path("<str:username>/address/default", views.DefaultAddressView.as_view()),
    # 邮件激活: v1/users/activation
    path("activation", views.active_view),
    # 短信验证码: v1/users/sms/code
    path("sms/code", views.sms_view),
    # 微博登录[获取code]: v1/users/weibo/authorization
    path("weibo/authorization", views.WeiBoCodeView.as_view()),
    # 微博登录[获取访问令牌access_token]: v1/users/weibo/users
    path("weibo/users", views.WeiBoTokenView.as_view()),
    # 绑定注册[已有用户请绑定]: weibo/users/binduser
    path("weibo/users/binduser", views.WeiBoBindView.as_view()),
]











