import time
from django.http import HttpResponse
from django.shortcuts import render


def server_view(request):
    if request.method == "GET":
        username = request.GET.get("username")
    elif request.method == "POST":
        username = request.POST.get("username")

    return HttpResponse(f"欢迎{username}")


def client_view(request):
    return render(request, "ajax.html")


def jq_client_view(request):

    return render(request, "jq_ajax.html")




