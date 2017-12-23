from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def block(request):
    #feed content put in json and add it in context
    
    ##Example of return with context##
    #context = {
    #    'coin_symbol': coin_symbol2,
    #    'latest_currency_list': latest_currency_list,
    #} 
    #return render(request, 'currencies/coin.html', context)
    #######################################################################
    return render(request, 'orderTrade/block.html')

def takeJSON(request):
    #feed content put in json and add it in context
    json_data = open('../json/history.json')
    data1 = json.load(json_data)

    ##Example of return with context##
    #context = {
    #    'coin_symbol': coin_symbol2,
    #    'latest_currency_list': latest_currency_list,
    #} 
    #return render(request, 'currencies/coin.html', context)
    #######################################################################
    return HttpResponse(
            json.dumps(data1),
            content_type="application/json"
        )