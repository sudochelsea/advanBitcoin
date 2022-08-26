from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
import requests 
from requests import RequestException

GHOST_KEY = settings.GHOST_KEY
BASE_URL = settings.BASE_URL
VERSION = settings.VERSION
LIMIT = settings.LIMIT

# i couldn't really figure how to do this, i just followed through on the old codebase

def index(request):
    page = request.GET.get('page_id', 1)
    posts = requests.get(
        f'''{BASE_URL}/{VERSION}/content/posts/?key={GHOST_KEY}&include=authors,tags&limit={LIMIT}&page={page}''')
    return render(request, 'blog/blog_homepage.html', {
            'posts': posts.json()['posts'],
            'pagination': posts.json()['meta']['pagination'],
        })
   


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

def blog(request):
    return render(request, "blog.html"),