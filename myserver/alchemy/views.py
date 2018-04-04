from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Elementos

def Index(request):
    elementos_list= Elementos.objects.all()
    return render(request, 'alchemy/index.html', {'elementos_list' : elementos_list})

def Mezclar(request):
    return render(request, 'alchemy/mezclar.html', {})

def Almacen(request):
    return render(request, 'alchemy/almacen.html', {})

# Create your views here.
