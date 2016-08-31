from django.db import models
from materia.models import Materia
from modulos.models import Disponibilidad

CONTRATO = (
('PA', 'PA'),
('PTC', 'PTC'),
('DC', 'Director de Carrera'),
)

class Maestro(models.Model):
  Nombre = models.CharField(max_length=50)
  Apellido_Paterno = models.CharField(max_length=50)
  Apellido_Materno = models.CharField(max_length=50)
  Contrato = models.CharField(choices= CONTRATO, max_length=3)
  Proyecto_Financiado = models.CharField(max_length=2)
  Grado_De_Estudio = models.CharField(max_length=50)
  Clase_Maestria = models.CharField(max_length=2)
  Num_Materias = models.SmallIntegerField()

class Maestro_Materia(models.Model):
  Id_Materia = models.ForeignKey(Materia)
  Id_Maestro = models.ForeignKey(Maestro)

 class Maestro_Disponibilidad(models.Model):
  Id_Maestro = models.ForeignKey(Maestro)
  Id_Disponibilidad = models.ForeignKey(Disponibilidad)
