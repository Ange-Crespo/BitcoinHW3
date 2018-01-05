from django.shortcuts import render

from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
      return render(request, 'mainpage/index.html')
    return HttpResponseRedirect('/user/login')
