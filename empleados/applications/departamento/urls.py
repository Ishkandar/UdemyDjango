from django.contrib import admin
from django.urls import path


def DesdeApps(self):
    print("=============IMPRIMIENDO DESDE APPS==============")


urlpatterns = [
    path('departamento/', DesdeApps),
]
