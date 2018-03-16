from django.shortcuts import render
from django.views.generic import TemplateView

class Index(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'alchemy/index.html', context=None)

# Create your views here.
