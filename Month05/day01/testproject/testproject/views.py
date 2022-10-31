from django.http import HttpResponse


def video_view(request):

    return HttpResponse("欢迎观看小泽视频")


def login_view(request):

    return HttpResponse("登录成功")


def index_view(request):
    return HttpResponse("这是我的首页")


def page1_view(request):
    return HttpResponse("这是编号为1的网页")




