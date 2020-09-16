from .views import *
from django.urls import path


urlpatterns = [
    path('prueba/', PruebaView.as_view()),
    path('lista/', PruebaListView.as_view()),
    path('lista-prueba/', ListarPrueba.as_view()),
    path('create-view-prueba/', PruebaCreateView.as_view())
]
