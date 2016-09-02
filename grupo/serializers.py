from rest_framework import serializers
from .models import Grupo

class GrupoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Grupo
    fields = ('id','Nombre', 'Tipo_Grupo','Id_Turno')
