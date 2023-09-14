from django.contrib import admin
from .models import *

# Register your models here.

#Fabrizio
#Utilizado3007

class DestinoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tiempo_vuelo_en_horas']
    search_fields = ['nombre', 'tiempo_vuelo_en_horas']
    list_filter = ['nombre', 'tiempo_vuelo_en_horas']

class AerolineaAdmin(admin.ModelAdmin):

    list_display = ['nombre']
    search_fields = ['nombre']
    list_filter = ['nombre']

class PilotoADmin(admin.ModelAdmin):

    list_display = ['nombre', 'apellido', 'tipo_licencia']
    search_fields = ['nombre', 'apellido', 'tipo_licencia']
    list_filter = ['nombre', 'apellido', 'tipo_licencia']

class AvionAdmin(admin.ModelAdmin):

    list_display = ['codigo', 'activo', 'aerolinea']
    search_fields = ['codigo', 'activo', 'aerolinea']
    list_filter = ['codigo', 'activo', 'aerolinea']


admin.site.register(Destino, DestinoAdmin)
admin.site.register(Aerolinea, AerolineaAdmin)
admin.site.register(Piloto, PilotoADmin)
admin.site.register(Avion, AvionAdmin)