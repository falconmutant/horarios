from rest_framework import serializers
from .models import *

class MaestroSerializer(serializers.ModelSerializer):
  class Meta:
    model = Maestro

class Maestro_Disponibilidad_Serializer(serializers.ModelSerializer):
  class Meta:
    model = Maestro_Disponibilidad

class Maestro_Materia_Serializer(serializers.ModelSerializer):
  class Meta:
    model = Maestro_Materia
