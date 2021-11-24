from django.shortcuts import render
from django.http import HttpResponse
from .models import post
# Create your views here.

def home(request):
    Post = {
        'posts': post.objects.all()
    }
    return render(request, 'blog/home.html', Post)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
    