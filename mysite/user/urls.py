from django.conf.urls import url
from django.contrib.auth.models import User

from . import views
from django.views.generic import TemplateView



app_name = 'user'
urlpatterns = [   
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^setting/$', views.setting, name='setting'),
    url(r'^deposit/$', views.deposit, name='deposit'),
    url(r'^withdraw/$', views.withdraw, name='withdraw'),
]
