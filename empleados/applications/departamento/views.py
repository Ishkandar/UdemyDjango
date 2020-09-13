from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Prueba2View(TemplateView):
    template_name = 'departamento/prueba_2.html'
