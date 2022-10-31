from django.http import HttpResponse
from django.shortcuts import render


def index_view(request):
    return HttpResponse("NBA:也是我现在正服下的毒药")
