from django.shortcuts import render

from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    if request.user.is_authenticated is False:
        return HttpResponseRedirect('/user/login')
    return render(request, 'mainpage/index.html')
