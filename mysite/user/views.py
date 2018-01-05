from django.shortcuts import render

from datetime import datetime  
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect

from mainpage.models import Account
# Create your views here.

def index(request):
    if request.user.is_authenticated: 
        account = Account.objects.get(user_id=request.user)
        return render(request, 'user/index.html', { 'balance': account.total_buy_sell_deposit_withdraw })
    return HttpResponseRedirect('/user/login')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, '', password)
        user.email = email
        user.save()
        user = auth.authenticate(username=username, password=password)
        account = Account.objects.create(user_id=user, creation_location="Taipei", last_password_modified_time=datetime.now(), last_login_ip="127.0.0.1", last_login_ip_location="Taipei", total_buy_sell_deposit_withdraw=0, phone_number="0912345678", national_id_proof="fake", first_name=username, last_name="Bithundi")
        account.save()
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/user')
        else:
            return HttpResponseRedirect('/user/login')
    else:
        if request.user.is_authenticated: 
            return HttpResponseRedirect('/user')
        return render(request, 'user/register.html')


def login(request):
    if request.user.is_authenticated: 
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

def setting(request):
    return render(request, 'user/setting.html')

def withdraw(request):
    account = Account.objects.get(user_id=request.user)
    account.total_buy_sell_deposit_withdraw -= int(request.POST.get("amount"))
    account.save()
    return HttpResponseRedirect('/user')

def deposit(request):
    account = Account.objects.get(user_id=request.user)
    account.total_buy_sell_deposit_withdraw += int(request.POST.get("amount"))
    account.save()
    return HttpResponseRedirect('/user')
