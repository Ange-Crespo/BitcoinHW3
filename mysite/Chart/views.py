import json
from django.http import HttpResponse
from django.shortcuts import render
from orderAndTrade.views import get_history

# Create your views here.

def index(request):
    data = get_history()
    result = {
        'code': 200,
        'data': data
    }
    return HttpResponse(json.dumps(result), content_type="application/json")
