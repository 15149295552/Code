from django.http import HttpResponse
from django.shortcuts import render


def birth_view(request):
    year, month, day = None, None, None

    if request.method == "GET":
        data = request.GET
        year = data.get("year")
        month = data.get("month")
        day = data.get("day")
    elif request.method == "POST":
        data = request.POST
        year = data.get("year")
        month = data.get("month")
        day = data.get("day")

    return HttpResponse(f"<h1>生日为:{year}年{month}月{day}日</h1>", content_type="text/plain;charset=utf-8", status=200)


class Cat:
    def __init__(self):
        self.color = "蓝色"
        self.name = "汤圆"

    def say(self):
        return "喵了个咪的~"


def index_view(request):
    username = "zhaoliying"
    # if标签
    stock = 50
    # for标签
    news_list = ["军事", "娱乐", "科技", "体育"]
    # 获取字典值
    dic = {"name": "茅台", "price": 7.66}
    # 函数
    def func():
        return "Small white rabbit white and white"

    # 对象
    mypet = Cat()

    return render(request, "index.html", locals())







