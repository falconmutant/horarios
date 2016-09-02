from rest_framework import serializers
from aula.models import *

class AulaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Aula
    fields = ('id','Nombre','Capacidad', 'Id_Tipo_de_aula', 'Id_Planta_Edificio')

class Aula_Disponibilidad_Serializer(serializers.ModelSerializer):
  class Meta:
      model = Aula_Disponibilidad
