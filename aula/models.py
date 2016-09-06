from django.db import models
from modulos.models import *
from materia.models import Materia
# Create your models here.
class Aula(models.Model):
    Nombre = models.TextField(null=False)
    Capacidad = models.TextField(null=False)
    Id_Tipo_de_aula = models.ForeignKey(Tipo_de_aula)
    Id_Planta_Edificio = models.ForeignKey(Planta_edificio)
    disponibilidad = models.ManyToManyField(Disponibilidad, through='Aula_Disponibilidad')
    def __str__(self):
        return "%s" % (self.Nombre)

class Aula_Disponibilidad(models.Model):
    Id_Disponibilidad = models.ForeignKey(Disponibilidad)
    Id_Aula = models.ForeignKey(Aula)
    def __str__(self):
        return "%s - %s" % (self.Id_Disponibilidad,self.Id_Aula)

class Aula_Software(models.Model):
    Id_Software = models.ForeignKey(Software)
    Id_Aula = models.ForeignKey(Aula)

class Aula_Materia(models.Model):
    Horas_Obligatorias =  models.SmallIntegerField()
    Peso = models.SmallIntegerField()
    Id_Aula = models.ForeignKey(Aula)
    Id_Materia = models.ForeignKey(Materia)
