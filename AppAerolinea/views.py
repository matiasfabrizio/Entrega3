from django.shortcuts import render

# Create your views here.

def inicio(req):

    return render(req, 'inicio.html')

def pilotos(req):

    return render(req, 'pilotos.html')