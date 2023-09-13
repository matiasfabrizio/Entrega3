from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('pilotos/', pilotos, name="Pilotos"),
    path('destinos/', destinos, name="Destinos"),
    path('aviones/', aviones, name="Aviones"),
    path('aerolineas/', aerolineas, name="Aerolineas"),

]
