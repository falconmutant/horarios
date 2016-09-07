from rest_framework import serializers
from aula.models import *

class AulaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Aula
