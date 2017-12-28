from django.shortcuts import render
from django.http import HttpResponse
import json as JSON
import subprocess
# Create your views here.

def get_bid_ask():
    json_data =subprocess.check_output(["./book","list"],cwd="../scripts")
    json_data=json_data.decode('utf-8')
    return JSON.loads(json_data)

def takeJSON_bid_ask(request):
    data1 = get_bid_ask()
    return HttpResponse(
            JSON.dumps(data1),
            content_type="application/json")
        

def get_history():
    json_data = subprocess.check_output(["./book","history", "0", "-1"],cwd="../scripts")
    json_data=json_data.decode('utf-8')
    return JSON.loads(json_data)
    
def takeJSON_history(request):
    data1 = get_history()

    return HttpResponse(
            JSON.dumps(data1),
            content_type="application/json"
        )
