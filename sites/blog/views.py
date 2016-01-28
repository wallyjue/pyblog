# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from .models import *

# import the logging library
import logging
import re

# Get an instance of a logger
logger = logging.getLogger('django')

# Create your views here.
def login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    logger.error('login page')
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
    category,blogtags,blog = get_tags_category(username)
    cat_pk = request.GET.get('cat', None)
    tag_name = request.GET.get('tag', None)
    post_list = []
    if cat_pk is not None:
        select_category = Category.objects.get(pk=cat_pk)
        post_list = Post.objects.filter(author = blog, category=select_category)
    elif tag_name is not None:
        tag_list = Tag.objects.filter(tag=tag_name)
        for tag in tag_list:
            post_list.append(tag.post)
    else:
        post_list = Post.objects.filter(author = blog)
        
    for post in post_list:
        post.media = Media.objects.filter(post = post)
        for media in post.media:
            if re.match('video', media.content_type):
                media.content = 'video'
            elif re.match('image', media.content_type):
                media.content = 'image'
            else:
                pass
        post.tags = Tag.objects.filter(post = post)

    return render(request, 'index.html', {
        'post_list': post_list,
        'blog': blog,
        'category':category,
        'blogtags':blogtags,
        })

def post_detail(request,username,pk):
    category,blogtags,blog = get_tags_category(username)
    post_list = Post.objects.filter(pk=pk)
    attachs = Media.objects.filter(post=post_list[0])
    return render(request, 'post.html', {
        'post_list': post_list,
        'blog': blog,
        'category':category,
        'blogtags':blogtags,
        'attachs':attachs
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
    category,blogtags,blog = get_tags_category(username)
    if request.user.is_authenticated():
        if request.method == "POST":
            post = Post.objects.get(pk=pk)
            title = request.POST.get('title', '')
            content = request.POST.get('content', '')
            category = Category.objects.get(name=request.POST.get('category', 'None'))
            tags = request.POST.getlist('tag')
            attachs = Media.objects.filter(post=post)
            post_list = Post.objects.filter(pk=pk)
            return render(request, 'post.html', {
                'post_list': post_list,
                'blog': blog,
                'category':category,
                'blogtags':blogtags,
                'attachs':attachs,
                'post':post,
                'tags':tags
                })
        else:    
            post = Post.objects.get(pk=pk)
            blog = post.author
            return render(request, 'edit.html', {
                'blog': blog,
                'category':category,
                'blogtags':blogtags,
                'post':post,
                })

def create_post(request):
    if request.method == "POST":
        if request.user.is_authenticated():
            user = User.objects.get(username=request.user.username)
            blog = Blog.objects.get( owner = user)
            post_list = Post.objects.filter(author = blog)
            title = request.POST.get('title', '')
            content = request.POST.get('content', '')
            category = Category.objects.get(name=request.POST.get('category', 'None'))
            tags = request.POST.getlist('tag')
            newpost = Post.objects.create(author = blog,title=title, content=content,category=category)
            for eachfile in request.FILES.getlist('docfile'):
                Media.objects.create(file = eachfile, post = newpost, content_type=eachfile.content_type)

            for key in tags:
                Tag.objects.create(post=newpost,tag=key)

            return render(request, 'index.html', {
                'post_list': post_list,
                'blog': blog,
                })
        else:
            return render(request, 'index.html', {})
    else:
        if request.user.is_authenticated():
            category,blogtags,blog = get_tags_category(request.user.username)
            tags = Tag.objects.all()
            return render(request, 'create.html', {
                'tags': tags,
                'category': category,
                'blog':blog,
                })

def get_tags_category(username):
    category = Category.objects.all()
    user = User.objects.get(username=username)
    blog = Blog.objects.get( owner = user)
    tagsets = set()
    for tag in Tag.objects.all():
        tagsets.add(tag.tag)
    return category,tagsets,blog
