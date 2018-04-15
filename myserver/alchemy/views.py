"""
Módulo de Django donde se conectan las clases
que representan las vistas, y sus archivos en 
html correspondientes
"""

from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Elementos

class Index(TemplateView):
    """Representa la vista principal"""

    def get(self, request, **kwargs):
        """Regresa la vista en html.

        Attributes:
            request: El request que se hizo al sevidor.
        Returns:
            El rendereo HTML de la vista principal.
        """
        elementos_list= Elementos.objects.all()
        return render(request, 'alchemy/index.html', {})

class Mezclar(TemplateView):
    """Representa la vista para mezclar."""

    def get(self, request, **kwargs):
        """Regresa la vista en html.

        Attributes:
            request: El request que se hizo al sevidor.
        Returns:
            El rendereo HTML de la vista para mezclar.
        """
        elementos_list = Elementos.objects.all()
        return render(request, 'alchemy/mezclar.html', {'elementos_list' : elementos_list})

class Almacen(TemplateView):
    """Representa la vista para el almacén."""

    def get(self, request, **kwargs):
        """Regresa la vista en html.

        Attributes:
            request: El request que se hizo al sevidor.
        Returns:
            El rendereo HTML de la vista para el almacén.
        """
        elementos_list = Elementos.objects.all()
        return render(request, 'alchemy/almacen.html', {'elementos_list' : elementos_list})
