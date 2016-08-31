from django.db import models
from modulos.models import Disponibilidad
from aula.models import Aula
from maestro.models import Maestro
from grupo.models import Grupo_Materia

class Solucion(models.Model):
  Costo = models.IntegerField()
  Id_Disponibilidad = models.ForeignKey(Disponibilidad)
  Id_Aula = models.ForeignKey(Aula)
  Id_Maestro = models.ForeignKey(Maestro)
  Id_Grupo_Materia = models.ForeignKey(Grupo_Materia)
