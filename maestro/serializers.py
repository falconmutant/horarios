from rest_framework import serializers
from .models import Maestro

class MaestroSerializer(serializers.ModelSerializer):
  class Meta:
    model = Maestro
    fields = ('Nombre', 'Apellido_Paterno', 'Apellido_Materno', 'Contrato',
      'Proyecto_Financiado', 'Grado_De_Estudio', 'Clase_Maestria',
      'Num_Materias')
