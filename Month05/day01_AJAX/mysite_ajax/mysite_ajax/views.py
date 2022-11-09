import time
from django.http import HttpResponse
from django.shortcuts import render


def server_view(request):
    if request.method == "GET":
        username = request.GET.get("username")
    elif request.method == "POST":
        username = request.POST.get("username")
    elif request.method == "PUT":
        # data: username=zhaoliying&age=18
        data = request.body.decode()
        username = data.split("&")[0].split("=")[1]
    elif request.method == "DELETE":
        # data: username=zhaoliying&age=18
        data = request.body.decode()
        username = data.split("&")[0].split("=")[1]

    return HttpResponse(f"{request.method}:{username}")


def client_view(request):

    return render(request, "ajax.html")


def jq_client_view(request):

    return render(request, "jq_ajax.html")







