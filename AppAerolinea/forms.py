from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class formPiloto(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    tipo_licencia = forms.IntegerField(
        #label='Nivel de Licencia',
        error_messages={'required':'Este campo es requerido.'}
    )


class formDestino(forms.Form):

    nombre = forms.CharField()
    tiempo_vuelo_en_horas = forms.IntegerField()


class formAerolineas(forms.Form):

    nombre = forms.CharField()


class formAviones(forms.Form):

    codigo = forms.IntegerField()
    activo = forms.BooleanField()
    aerolinea = forms.CharField()