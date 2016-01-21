from django.shortcuts import render
from django.contrib import auth

# Create your views here.
def login(request):

    if request.user.is_authenticated(): 
        return render(request, 'index.html', {})

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return render(request, 'index.html', {})
    else:
        return render(request, 'login.html', {})

def logout(request):
    auth.logout(request)
    return render(request, 'index.html', {})

def index(request):
    return render(request, 'index.html', {})