from django.shortcuts import render
from django.views.generic import (TemplateView,
                                  ListView,
                                  CreateView)
# import models
from .models import Prueba

# Create your views here.
class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class PruebaListView(ListView):
    template_name = 'home/lista.html'
    context_object_name = 'listaNumeros'
    queryset = ['0', '10', '20', '30']


class ListarPrueba(ListView):
    template_name = 'home/lista_prueba.html'
    context_object_name = 'listaPrueba'
    model = Prueba


class PruebaCreateView(CreateView):
    template_name = 'home/create_view_prueba.html'
    model = Prueba
    fields = ['titulo', 'subtitulo', 'cantidad']


# TODO: es de prueba