from django.db import models
from modulos.models import *
# Create your models here.
class Aula(models.Model):
	Nombre = models.TextField(null=False)
	Capacidad = models.TextField(null=False)
	Id_Tipo_de_aula = models.ForeignKey(Tipo_de_aula)
	Id_Planta_Edificio = models.ForeignKey(Planta_edificio)
	def __str__(self):
		return "%s" % (self.Nombre)

class Aula_disponibilidad(models.Model):
	Id_Disponibilidad = models.ForeignKey(Disponibilidad)
	Id_Aula = models.ForeignKey(Aula)

class Aula_software(models.Model):
	Id_Software = models.ForeignKey(Software)
	Id_Aula = models.ForeignKey(Aula)