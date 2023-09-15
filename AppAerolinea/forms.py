from django import forms
from .models import Aerolinea
from django.core.validators import MinValueValidator, MaxValueValidator

class formPiloto(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    tipo_licencia = forms.IntegerField(
        validators=[
            MinValueValidator(1, message="El número mínimo de licencia es 1."),
            MaxValueValidator(30, message="El número máximo de licencia es 4.")
        ]
    )


class formDestino(forms.Form):

    nombre = forms.CharField()
    tiempo_vuelo_en_horas = forms.IntegerField(
        validators=[
            MinValueValidator(1, message="El número mínimo de horas es 1."),
            MaxValueValidator(30, message="El número máximo de horas es 30.")
        ]
    )


class formAerolineas(forms.Form):

    nombre = forms.CharField()


class formAviones(forms.Form):

    opciones = Aerolinea.objects.all().values_list('id', 'nombre')

    codigo = forms.IntegerField()
    activo = forms.BooleanField()
    aerolinea = forms.ChoiceField(choices=opciones)