from django.contrib import admin
from django.urls import path


def DesdeApps2(self):
    print("===============IMPRIMIENDO DESDE APPS 2==================")


urlpatterns = [
    path('persona/', DesdeApps2),
]
