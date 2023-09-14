from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('pilotos/', pilotos, name="Pilotos"),
    path('destinos/', destinos, name="Destinos"),
    path('aviones/', aviones, name="Aviones"),
    path('aerolineas/', aerolineas, name="Aerolineas"),
    path('pilotosFormulario/', pilotosFormulario, name="PilotosFormulario"),
    path('destinosFormulario/', destinosFormulario, name="DestinosFormulario"),
    path('avionesFormulario/', avionesFormulario, name="AvionesFormulario"),
]
