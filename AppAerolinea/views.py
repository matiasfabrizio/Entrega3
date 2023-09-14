from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.

def inicio(req):

    if req.method == "GET" or req.method == "POST":

        context = {
            'pag_inicio' : True,
        }
        return render(req, 'inicio.html', context)
    
    else:

        context = {
            'pag_inicio' : True,
        }
        return render(req, 'inicio.html', context)


def pilotos(req):
    
    lista = Piloto.objects.all()

    return render(req, 'pilotos.html', {'pilotos':lista})


def pilotosFormulario(req):

    lista = Piloto.objects.all()

    if req.method == "POST":
        
        mi_formulario = formPiloto(req.POST)

        
        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data

            piloto = Piloto(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], tipo_licencia=data["tipo_licencia"])
            piloto.save()

            return render(req, 'pilotos.html', {'pilotos':lista})

    else:
        
        mi_formulario = formPiloto()

    return render(req, 'pilotosFormulario.html', {"mi_formulario": mi_formulario})


def destinos(req):

    lista = Destino.objects.all()

    return render(req, 'destinos.html', {'destinos':lista})


def destinosFormulario(req):

    lista = Destino.objects.all()

    if req.method == "POST":
        
        mi_formulario = formDestino(req.POST)

        
        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data

            destino = Destino(nombre=data["nombre"], tiempo_vuelo_en_horas=data["tiempo_vuelo_en_horas"])
            destino.save()

            return render(req, 'destinos.html', {'destinos':lista})

    else:
        
        mi_formulario = formDestino()

    return render(req, 'destinosFormulario.html', {"mi_formulario": mi_formulario})


def aviones(req):

    lista = Avion.objects.all()

    return render(req, 'aviones.html', {'aviones':lista})

def avionesFormulario(req):

    lista = Avion.objects.all()

    if req.method == "POST":
        
        mi_formulario = formAviones(req.POST)

        
        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data

            avion = Avion(codigo=data["codigo"], activo=data["activo"], aerolinea=data["aerolinea"])
            avion.save()

            return render(req, 'aviones.html', {'aviones':lista})

    else:
        
        mi_formulario = formAviones()

    return render(req, 'avionesFormulario.html', {"mi_formulario": mi_formulario})


def aerolineas(req):

    lista = Aerolinea.objects.all()

    return render(req, 'aerolineas.html', {'aerolineas':lista})

def aerolineasFormulario(req):

    lista = Aerolinea.objects.all()

    if req.method == "POST":
        
        mi_formulario = formAerolineas(req.POST)
        
        if mi_formulario.is_valid():
            
            data = mi_formulario.cleaned_data

            aerolinea = Aerolinea(nombre=data["nombre"])
            aerolinea.save()

            return render(req, 'aerolineas.html', {'aerolineas':lista})

    else:
        
        mi_formulario = formAerolineas()

    return render(req, 'aerolineasFormulario.html', {"mi_formulario": mi_formulario})