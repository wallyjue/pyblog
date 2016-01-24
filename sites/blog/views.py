# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from .models import *

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return blog_detail(request,username)
    else:
        return render(request, 'login.html', {})

def logout(request):
    auth.logout(request)
    return render(request, 'login.html', {})

def index(request):
    return render(request, 'index.html', {})

def blog_detail(request,username):
    user = User.objects.get(username=username)
    blog = Blog.objects.filter( owner = user)
    post_list = Post.objects.filter(author = blog[0])
    for post in post_list:
        tags = Tag.objects.filter( post = post)
        post.tags = tags
        
    return render(request, 'index.html', {
        'post_list': post_list,
        'blog': blog[0],
        })

def post_detail(request,username,pk):
    #if request.user.is_authenticated() != True: 
    #    return render(request, 'index.html', {})
    user = User.objects.get(username=username)
    blog = Blog.objects.filter( owner = user)
    post_list = Post.objects.filter(pk=pk)
    for post in post_list:
        tags = Tag.objects.filter( post = post)
        post.tags = tags

    return render(request, 'post.html', {
        'post_list': post_list,
        'blog': blog,
        })

def delete_post(request,username,pk):
	if request.user.is_authenticated():
		post = Post.objects.get(pk=pk)
		blog = post.author
		post.delete()
		return render(request, 'ok.html', {
        	'blog': blog,
        	})

def edit_post(request,username,pk):
    if request.user.is_authenticated():
        return render(request, 'ok.html', {})

def create_post(request):
    if request.method == "POST":
        if request.user.is_authenticated():
            user = User.objects.get(username=request.user.username)
            blog = Blog.objects.filter( owner = user)
            post_list = Post.objects.filter(author = blog)
            title = request.POST.get('title', '')
            content = request.POST.get('content', '')
            category = request.POST.get('category', '')
            content = request.POST.get('content', '')
            medias = request.POST.getlist('media')
            tags = request.POST.getlist('tag')
            newpost = Post.objects.create(author = blog[0],title=title, content=content)
            for key in tags:
                Tag.objects.create(post=newpost,tag=key)
            for key in medias:
                Media.objects.create(post=newpost,mediafile=key)

            return render(request, 'index.html', {
                'post_list': post_list,
                'blog': blog,
                })
        else:
            return render(request, 'index.html', {})
    else:
        tags = Tag.objects.all()
        category = Category.objects.all()
        return render(request, 'create.html', {
            'tags': tags,
            'category': category,
            })
