import json
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    result = {
        "code": 200,
        "data": [
            {
                'symbol': "btc", 'last': 323, 'percent': 53, 'volume': 600
            },
            {
                'symbol': "eth", 'last': 345, 'percent': 34, 'volume': 567
            },
            {
                'symbol': "ltc", 'last': 567, 'percent': 67, 'volume': 456
            },
            {
                'symbol': "dash", 'last': 234, 'percent': 23, 'volume': 890
            },
            {
                'symbol': "dash", 'last': 234, 'percent': 23, 'volume': 890
            },
            {
                'symbol': "zec", 'last': 111, 'percent': 78, 'volume': 345
            }
        ]
    }
    return HttpResponse(json.dumps(result), content_type="application/json")
