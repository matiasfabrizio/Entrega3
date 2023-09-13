from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class formPiloto(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    tipo_licencia = forms.IntegerField()


class formDestino(forms.Form):

    nombre = forms.IntegerField()
    tiempo_vuelo_en_horas = forms.IntegerField()