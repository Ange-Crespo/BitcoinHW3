from django.shortcuts import render

from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request, 'user/index.html')


def register(request):
    if request.method == "POST":
        return HttpResponse('POST')
    else:
        return render(request, 'user/register.html')


def login(request):
    if request.user.is_authenticated(): 
        return HttpResponseRedirect('/user')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/user')
    else:
        return render(request, 'user/login.html') 


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/user/login')
