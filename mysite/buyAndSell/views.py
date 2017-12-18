from django.shortcuts import render

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