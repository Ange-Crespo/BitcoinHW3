from django.conf.urls import url

from . import views
from django.views.generic import TemplateView



app_name = 'orderAndtrade'
urlpatterns = [   
    url(r'^json/bid_ask$', views.takeJSON_bid_ask, name='bid_ask'), 
    url(r'^json/history$', views.takeJSON_history, name='history'), 
]
