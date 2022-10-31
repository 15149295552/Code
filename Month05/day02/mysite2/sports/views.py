from django.http import HttpResponse
from django.shortcuts import render


def index_view(request):
    return HttpResponse("sports:也许时间是一种解药")


