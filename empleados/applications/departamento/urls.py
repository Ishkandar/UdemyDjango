from .views import *
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('departamento/', Prueba2View.as_view()),
]
