from django.shortcuts import render
from django.http import HttpResponse, HttpRequest




def index(request):
    return render(request, "core/index.html", name="index")

def about(request):
    return render(request, "core/about.html", name="about")

def base(request):
    return render(request, "core/base.html", name="base")
