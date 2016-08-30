from django.db import models

class Maestro(models.Model):
  Nombre = models.CharField(max_length=50)
  Apellido_Paterno = models.CharField(max_length=50)
  Apellido_Materno = models.CharField(max_length=50)
  Contrato = models.CharField(max_length=50)
  Proyecto_Financiado = models.CharField(max_length=2)
  Grado_De_Estudio = models.CharField(max_length=50)
  Clase_Maestria = models.CharField(max_length=2)
  Num_Materias = models.SmallIntegerField()
