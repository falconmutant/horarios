from django.db import models
from modulos.models import Cuatrimestre

class Materia(models.Model):
  Nombre = models.CharField(max_length=70)
  Horas_Por_Semana = models.SmallIntegerField()
  Id_Cuatrimestre = models.ForeignKey(Cuatrimestre)
