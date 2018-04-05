from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Elementos

class Index(TemplateView):

    def get(self, request, **kwargs):
        elementos_list= Elementos.objects.all()
        return render(request, 'alchemy/index.html', {})

class Mezclar(TemplateView):

    def get(self, request, **kwargs):
        return render(request, 'alchemy/mezclar.html', {})

class Almacen(TemplateView):

    def get(self, request, **kwargs):
        elementos_list = Elementos.objects.all()
        return render(request, 'alchemy/almacen.html', {'elementos_list' : elementos_list})

# Create your views here.
