from django import forms
from .models import Aerolinea

class formPiloto(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    tipo_licencia = forms.IntegerField()


class formDestino(forms.Form):

    nombre = forms.CharField()
    tiempo_vuelo_en_horas = forms.IntegerField()


class formAerolineas(forms.Form):

    nombre = forms.CharField()


class formAviones(forms.Form):

    opciones = Aerolinea.objects.all().values_list('id', 'nombre')

    codigo = forms.IntegerField()
    activo = forms.BooleanField()
    aerolinea = forms.ChoiceField(choices=opciones)