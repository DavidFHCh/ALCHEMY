"""
Módulo de Django en el cual se especifican
las rutas que existirán dentro del sitio
"""

from django.conf.urls import include, url
from django.urls import path
from alchemy import views

urlpatterns = [
        # Tenemos 3 rutas para 3 vistas, la vista principal
        # de inicio, la vista para mezclar, y la vista para
        # tomar elementos del almacén.
        url(r'^$', views.Index.as_view()),
        url(r'^mezclar/', views.Mezclar.as_view()),
        url(r'^almacen/', views.Almacen.as_view())
    ]
