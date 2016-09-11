from django.db import models
from materia.models import Materia
from modulos.models import Disponibilidad

CONTRATO = (
  ('PA', 'PA'),
  ('PTC', 'PTC'),
  ('DC', 'Director de Carrera'),
)
FINANCIADO = (
  ('P', 'PE'),
  ('N', 'NO'),
  ('I', 'IN'),
)
GRADO = (
  ('M', 'MESTRIA'),
  ('D', 'DOCTORADO'),
  ('L', 'LICENCIATURA'),
)
SI_NO = (
  ('S', 'SI'),
  ('N', 'NO'),
)

class Maestro(models.Model):
  Nombre = models.CharField(max_length=50)
  Apellido_Paterno = models.CharField(max_length=50)
  Apellido_Materno = models.CharField(max_length=50)
  Contrato = models.CharField(choices= CONTRATO, max_length=3)
  Proyecto_Financiado = models.CharField(choices= FINANCIADO, max_length=1)
  Grado_De_Estudio = models.CharField(choices= CONTRATO, max_length=1)
  Clase_Maestria = models.CharField(choices= SI_NO, max_length=1)
  Num_Materias = models.SmallIntegerField()
  materias= models.ManyToManyField(Materia, through='Maestro_Materia')
  disponibilidad= models.ManyToManyField(Disponibilidad, through='Maestro_Disponibilidad')

class Maestro_Materia(models.Model):
  Id_Materia = models.ForeignKey(Materia)
  Id_Maestro = models.ForeignKey(Maestro)

class Maestro_Disponibilidad(models.Model):
  Id_Maestro = models.ForeignKey(Maestro)
  Id_Disponibilidad = models.ForeignKey(Disponibilidad)
