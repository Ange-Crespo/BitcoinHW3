import json
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import buyAndSellForm

import os

# Create your views here.
def content(request):
    #feed content put in json and add it in context
    
    ##Example of return with context##
    #context = {
    #    'coin_symbol': coin_symbol2,
    #    'latest_currency_list': latest_currency_list,
    #} 
    #return render(request, 'currencies/coin.html', context)
    #######################################################################

    
    return render(request, 'buyAndSell/content.html')


'''def form(request) :

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = buyAndSellForm(request.POST)
        # check whether it's valid:
        print(form.errors)
        message = "Something went Wrong, Try Again please"
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print(form.cleaned_data["Amount"])
            message = "Your order is Sended"
        
        return HttpResponse((json.dumps({'message': message})))
    else:
        form = buyAndSellForm()

    return HttpResponse(print(form.errors))'''

def create_post(request):
    if request.method == 'POST':
        Limit = request.POST.get('Limit')
        amount = request.POST.get('amount')
        price = request.POST.get('price')
        cmd = request.POST.get('cmd')
        print(cmd)
        response_data = {}
        os.system("pwd && cd ../scripts && pwd && ./book "+cmd+" "+price+" "+amount)
        #&& cd ../script && book > "+ cmd +" "+price+" "+amount)

        
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )