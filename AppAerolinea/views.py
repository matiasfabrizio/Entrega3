from django.shortcuts import render

# Create your views here.

def inicio(req):

    context = {
        'pag_inicio' : True,
    }
    return render(req, 'inicio.html', context)

def pilotos(req):

    return render(req, 'pilotos.html')

def destinos(req):

    return render(req, 'destinos.html')

def aviones(req):

    return render(req, 'aviones.html')

def aerolineas(req):

    return render(req, 'aerolineas.html')