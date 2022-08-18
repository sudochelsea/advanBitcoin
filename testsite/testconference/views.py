from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# def index(request):
#     return HttpResponse("Hello, conference")


def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def speakers(request):
    return render(request, "speakers.html")


def sponsors(request):
    return render(request, "sponsors.html")