from rest_framework import serializers
from .models import Materia

class MateriaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Materia
    fields = ('Nombre', 'Horas_Por_Semana', 'Id_Cuatrimestre')
