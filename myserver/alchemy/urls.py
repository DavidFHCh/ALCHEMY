from django.conf.urls import include, url
from django.urls import path
from alchemy import views

urlpatterns = [
        url(r'^$', views.Index.as_view()),
        url(r'^mezclar/', views.Mezclar.as_view()),
        url(r'^almacen/', views.Almacen.as_view())
    ]
