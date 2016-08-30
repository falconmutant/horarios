from django.db import models

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
