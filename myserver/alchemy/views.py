from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("In the future this will be a beautiful site.")

# Create your views here.
