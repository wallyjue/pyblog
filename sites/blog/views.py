from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Post,Blog

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
    return render(request, 'index.html', {})

def index(request):
    return render(request, 'index.html', {})

def blog_detail(request,username):
    user = User.objects.get(username=username)
    blog = Blog.objects.filter( owner = user)
    post_list = Post.objects.filter(author = blog)
    return render(request, 'index.html', {
        'post_list': post_list,
        'blog': blog,
        })

def post_detail(request,username,pk):
    #if request.user.is_authenticated() != True: 
    #    return render(request, 'index.html', {})

    user = User.objects.get(username=username)
    blog = Blog.objects.filter( owner = user)
    post_list = Post.objects.filter(pk=pk)
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