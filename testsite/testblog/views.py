from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
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
   