from rest_framework import serializers
from aula.models import Aula

class AulaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Aula
    fields = ('Nombre','Capacidad')
