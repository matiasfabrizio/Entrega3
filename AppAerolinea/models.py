from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Destino(models.Model):

    nombre = models.CharField(max_length=60)
    tiempo_vuelo_en_horas = models.IntegerField(max_length=2, validators=[
        MinValueValidator(1, message='El tiempo mínimo de vuelo es 1 hora.'),
        MaxValueValidator(30, message='El vuelo más largo posible es de 30 horas.') #El dato lo saqué de internet.
    ])

    def __str__(self):
        return f'{self.nombre}'
    
    class Meta():

        verbose_name = 'Destiny'
        verbose_name_plural = 'Destinations'


class Aerolinea(models.Model):

    nombre = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.nombre}'
    
    class Meta():

        verbose_name = 'Airline'
        verbose_name_plural = 'Airlines'


#Me apoyé de chat gtp para el Min y Max values
class Piloto(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    tipo_licencia = models.IntegerField(validators=[
        MinValueValidator(1, message='El nivel mínimo debe ser 1.'),
        MaxValueValidator(4, message='El nivel máximo debe ser 4.')
    ])


    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
    class Meta():

        verbose_name = 'Pilot'
        verbose_name_plural = 'Pilots'


#Los valores predeterminados los saqué de la siguiente forma:
    # Fecha de creación > Lo saqué de la clase de Mauricio.
    # Activo > Lo saqué de foros al recibir un error trabajando cuando copiaba copiar el código de la clase.
class Avion(models.Model):

    codigo = models.IntegerField(max_length=12)
    activo = models.BooleanField(default=False)
    aerolinea = models.ForeignKey(Aerolinea, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.codigo} - {self.activo}'
    
    class Meta():

        verbose_name = 'Plane'
        verbose_name_plural = 'Planes'

