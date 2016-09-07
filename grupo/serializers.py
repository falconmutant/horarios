from rest_framework import serializers
from .models import *

class GrupoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Grupo

class Grupo_Materia_Serializer(serializers.ModelSerializer):
  class Meta:
    model = Grupo_Materia
