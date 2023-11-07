from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class IndexPageView(TemplateView):
    template_name = 'home_module/index.html'
