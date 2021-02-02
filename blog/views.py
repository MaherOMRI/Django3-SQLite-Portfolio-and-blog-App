from django.shortcuts import render, get_object_or_404
from .models import *
from portfolio.models import Project

def all_blogs(request):
    projects = Project.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogs': blogs,'projects': projects})

def detail(request, blog_id):
    slectedblog = get_object_or_404(Blog, pk=blog_id)
    blogs = Blog.objects.all()
    return render(request, 'blog/detail.html', {'slectedblog': slectedblog})


