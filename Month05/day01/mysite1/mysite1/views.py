from django.http import HttpResponse


def index_view(request):
    return HttpResponse("<h1>首页</h1>")


def page1_view(request):
    return HttpResponse("编号为1的网页")


def page2_view(request):
    return HttpResponse("编号为2的网页")


# path("page/<int:page_num>", views.....)
def page_view(request, page_num):

    return HttpResponse(f"编号为{page_num}的网页")


def cal_view(request, x, operation, y):
    if operation == "add":
        result = x + y
    elif operation == "sub":
        result = x - y
    elif operation == "mul":
        result = x * y
    elif operation == "div":
        result = x / y
    else:
        result = "无效的操作"

    return HttpResponse(f"结果:{result}")


def login_view(request):
    # request:请求头、请求体、请求方法... ...
    # 1. method属性：请求方法
    print("method:", request.method)
    # 2. GET属性:查询字符串
    # http://127.0.0.1:8000/v1/users/login?username=xxx&password=xxx
    print("GET属性:", request.GET)
    print("username:", request.GET.get("username"))
    print("password:", request.GET.get("password"))

    # 3.POST属性:获取请求体(<QueryDict: {}>)
    #   POST属性:以表单形式提交的
    print("POST属性:", request.POST)
    # 4.body属性:获取请求体(b"")
    #   body属性:数据以json形式提交
    print("body属性:", request.body)

    # 5.META属性:获取请求头等信息
    #   会把所有的请求头都大写,并加上HTTP_前缀
    print("META属性:", request.META)

    return HttpResponse("九霄龙吟惊天变,登录成功")







