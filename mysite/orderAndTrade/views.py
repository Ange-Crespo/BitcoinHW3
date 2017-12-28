from django.shortcuts import render
from django.http import HttpResponse
import json as JSON
import subprocess
# Create your views here.

def takeJSON_bid_ask(request):
    #feed content put in json and add it in context
    json_data =subprocess.check_output(["./book","list"],cwd="../scripts")
    #print(json_data.decode('utf-8'))
    json_data=json_data.decode('utf-8')
    #print(json_data)
    data1 = JSON.loads(json_data)
    return HttpResponse(
            JSON.dumps(data1),
            content_type="application/json")
        

def takeJSON_history(request):
    #feed content put in json and add it in context
    json_data = subprocess.check_output(["./book","history", "0", "-1"],cwd="../scripts")
    json_data=json_data.decode('utf-8')
    print(json_data)
    data1 = JSON.loads(json_data)

    return HttpResponse(
            JSON.dumps(data1),
            content_type="application/json"
        )