from django.db import models
from modulos.models import Turno
from materia.models import Materia

TIPO = (
	('O', 'ORDINARIO'),
	('E', 'ESPECIAL'),
	('D', 'DISTANCIA'),
)

class Grupo(models.Model):
  Nombre = models.TextField(max_length=50, null=False)
  Tipo_Grupo = models.CharField(choices= TIPO, max_length=1)
  Id_Turno = models.ForeignKey(Turno)
  materias = models.ManyToManyField(Materia, through='Grupo_Materia')

class Grupo_Materia(models.Model):
  Id_Materia = models.ForeignKey(Materia)
  Id_Grupo = models.ForeignKey(Grupo)
