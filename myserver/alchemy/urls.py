from django.conf.urls import include, url
from django.urls import path
from alchemy import views

urlpatterns = [
        url(r'^$', views.Index),
        url(r'^mezclar/$', views.Mezclar, name = 'Mezclar')
    ]
