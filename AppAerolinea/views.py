from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.

def inicio(req):

    context = {
        'pag_inicio' : True,
    }
    return render(req, 'inicio.html', context)


def pilotos(req):
    
    return render(req, 'pilotos.html')


def pilotosFormulario(req):
    if req.method == "POST":
        
        mi_formulario = formPiloto(req.POST)

        
        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data

            piloto = Piloto(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], tipo_licencia=data["tipo_licencia"])
            piloto.save()

            return render(req, 'inicio.html')

    else:
        
        mi_formulario = formPiloto()

    return render(req, 'pilotosFormulario.html', {"mi_formulario": mi_formulario})


def destinos(req):

    return render(req, 'destinos.html')

def aviones(req):

    return render(req, 'aviones.html')

def aerolineas(req):

    return render(req, 'aerolineas.html')