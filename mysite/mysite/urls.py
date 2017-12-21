"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$',include('mainpage.urls')),
    url(r'^alert/',include('alert.urls')),
    url(r'^buyAndSell/',include('buyAndSell.urls')),
    url(r'^Chart/',include('Chart.urls')),
    url(r'^orderSell/',include('orderSell.urls')),
    url(r'^orderBuy/',include('orderBuy.urls')),
    url(r'^orderTrade/',include('orderTrade.urls')),
    url(r'^tickers/',include('tickers.urls')),
    url(r'^titleCurrencie/',include('titleCurrencie.urls')),
    url(r'^mainpage/',include('mainpage.urls')),
    url(r'^landpage/', include('landpage.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^admin/', admin.site.urls),
]
