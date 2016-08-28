from django.db import models

# Create your models here.
class Software(models.Model):
	Nombre = models.TextField(max_length=30, null=False)

class Planta(models.Model):
	Planta = models.TextField(max_length=10, null=False)

class Edificio(models.Model):
	Nombre_Edificio = models.TextField(max_length=50, null=False)

class Tipo_de_aula(models.Model):
	Nombre = models.TextField(max_length=30, null=False)

class Dia(models.Model):
	Dia = models.TextField(max_length=10, null=False)

class Hora(models.Model):
	Hora = models.IntegerField(null=False)

class Carrera(models.Model):
	Carrera = models.TextField(max_length=45, null=False)

class Turno(models.Model):
	Turno = models.TextField(max_length=15, null=False)

class Pantaedificio(models.Model):
	Id_Planta = models.ForeignKey(Planta)
	Id_Edificio = models.ForeignKey(Edificio)

class Disponibilidad(models.Model):
	Id_Hora = models.ForeignKey(Hora)
	Id_Dia = models.ForeignKey(Dia)

class Cuatrimestre(models.Model):
	Cuatrimestre = models.TextField(null=False)
	Id_Carrera = models.ForeignKey(Carrera)