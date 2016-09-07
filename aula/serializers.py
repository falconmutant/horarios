from rest_framework import serializers
from aula.models import *

class AulaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Aula

class Aula_Disponibilidad_Serializer(serializers.ModelSerializer):
  class Meta:
    model = Aula_Disponibilidad

class Aula_Software_Serializer(serializers.ModelSerializer):
  class Meta:
    model = Aula_Software

class Aula_Materia_Serializer(serializers.ModelSerializer):
  class Meta:
    model = Aula_Materia
