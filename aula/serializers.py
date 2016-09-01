from rest_framework import serializers
from aula.models import Aula

class AulaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Aula
    fields = ('id','Nombre','Capacidad', 'Id_Tipo_de_aula', 'Id_Planta_Edificio')
