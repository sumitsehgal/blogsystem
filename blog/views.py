from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'blogs/posts/index.html', {'posts': posts})

def index2(request):
    return render(request, 'blogs/index.html')

def individual_post(request, id):
    recent_post = Post.objects.get(id__exact=id)
    return render(request, 'blogs/posts/detail.html', {'post':recent_post})
