from rest_framework import serializers
from .models import *

class SolucionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Solucion
