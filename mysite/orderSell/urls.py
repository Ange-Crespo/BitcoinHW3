from django.conf.urls import url

from . import views
from django.views.generic import TemplateView



app_name = 'orderSell'
urlpatterns = [   
    url(r'^content/$', views.content, name='content'), 
]