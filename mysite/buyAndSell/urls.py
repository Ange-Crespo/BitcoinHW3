from django.conf.urls import url

from . import views
from django.views.generic import TemplateView



app_name = 'buyAndSell'
urlpatterns = [   
    url(r'^create_post/$', views.create_post, name='create_post'), 
]