from django.shortcuts import render

from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
<<<<<<< Updated upstream
    if request.user.is_authenticated() is False:
        return HttpResponseRedirect('/user/login')
=======
    #if request.user.is_authenticated() is False:
    #    return HttpResponseRedirect('/user/login')
>>>>>>> Stashed changes
    return render(request, 'mainpage/index.html')
