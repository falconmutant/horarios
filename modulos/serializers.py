from rest_framework import serializers
from .models import *

class SoftwareSerializer(serializers.ModelSerializer):
  class Meta:
    model = Software
    fields = ('id', 'Nombre',)

class PlantaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Planta
    fields = ('id', 'Planta',)

class EdificioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Edificio
    fields = ('id', 'Nombre_Edificio',)

class Tipo_de_aulaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tipo_de_aula
    fields = ('id', 'Nombre',)

class DiaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dia
    fields = ('id', 'Dia',)

class HoraSerializer(serializers.ModelSerializer):
  class Meta:
    model = Hora
    fields = ('id', 'Hora',)

class CarreraSerializer(serializers.ModelSerializer):
  class Meta:
    model = Carrera
    fields = ('id', 'Carrera',)

class TurnoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Turno
    fields = ('id', 'Turno',)

class DisponibilidadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Disponibilidad

class CuatrimestreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cuatrimestre
    fields = ('id', 'Cuatrimestre', 'Id_Carrera')
