import json
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    json_data = open('../json/history.json')
    data = json.load(json_data)
    result = {
        'code': 200,
        'data': data
    }
    return HttpResponse(json.dumps(result), content_type="application/json")
