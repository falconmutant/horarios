from django.db import models

# Create your models here.
class Software(models.Model):
	Nombre = models.TextField(max_length=30, null=False)
	def __str__(self):
		return "%s" % (self.Nombre)

class Planta(models.Model):
	Planta = models.TextField(max_length=10, null=False)
	def __str__(self):
		return "%s" % (self.Planta)

class Edificio(models.Model):
	Nombre_Edificio = models.TextField(max_length=50, null=False)
	def __str__(self):
		return "%s" % (self.Nombre_Edificio)

class Tipo_de_aula(models.Model):
	Nombre = models.TextField(max_length=30, null=False)
	def __str__(self):
		return "%s" % (self.Nombre)

class Dia(models.Model):
	Dia = models.TextField(max_length=10, null=False)
	def __str__(self):
		return "%s" % (self.Dia)

class Hora(models.Model):
	Hora = models.IntegerField(null=False)
	def __str__(self):
		return "%s" % (self.Hora)

class Carrera(models.Model):
	Carrera = models.TextField(max_length=45, null=False)
	def __str__(self):
		return "%s" % (self.Carrera)

class Turno(models.Model):
	Turno = models.TextField(max_length=15, null=False)
	def __str__(self):
		return "%s" % (self.Turno)

class Planta_edificio(models.Model):
	Id_Planta = models.ForeignKey(Planta)
	Id_Edificio = models.ForeignKey(Edificio)
	def __str__(self):
		return "%s-%s" % (self.Id_Planta,self.Id_Edificio)

class Disponibilidad(models.Model):
	Id_Hora = models.ForeignKey(Hora)
	Id_Dia = models.ForeignKey(Dia)
	def __str__(self):
		return "%s-%s" % (self.Id_Hora,self.Id_Dia)

class Cuatrimestre(models.Model):
	Cuatrimestre = models.SmallIntegerField()
	Id_Carrera = models.ForeignKey(Carrera)
	def __str__(self):
		return "%s-%s" % (self.Cuatrimestre,self.Id_Carrera)