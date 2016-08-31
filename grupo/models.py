from django.db import models
from modulos.models import Turno
from materia.models import Materia

class Grupo(models.Model):
  Nombre = models.TextField(max_length=50, null=False)
  Tipo_Grupo = models.TextField(max_length=15,null=False)
  Id_Turno = models.ForeignKey(Turno)

class Grupo_Materia(models.Model):
  Id_Materia = models.ForeignKey(Materia)
  Id_Grupo = models.ForeignKey(Grupo)
