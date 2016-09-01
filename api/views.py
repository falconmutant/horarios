from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from aula.serializers import AulaSerializer
from aula.models import Aula
from grupo.serializers import GrupoSerializer
from grupo.models import Grupo
from maestro.serializers import MaestroSerializer
from maestro.models import Maestro
from materia.serializers import MateriaSerializer
from materia.models import Materia
from modulos.serializers import *
from modulos.models import *
from panel.serializers import *
from panel.models import *

class AulaList(APIView):
  def get(self, request, format=None):
    aula = Aula.objects.all()
    serializer = AulaSerializer(aula,many = True)
    return Response(serializer.data)

class GrupoList(APIView):
  def get(self, request, format=None):
    grupo = Grupo.objects.all()
    serializer = GrupoSerializer(grupo,many = True)
    return Response(serializer.data)

class MaestroList(APIView):
  def get(self, request, format=None):
    maestro = Maestro.objects.all()
    serializer = MaestroSerializer(maestro, many = True)
    return Response(serializer.data)

class MateriaList(APIView):
  def get(self, request, format=None):
    materia = Materia.objects.all()
    serializer = MateriaSerializer(materia,many=True)
    return Response(serializer.data)

class SoftwareList(APIView):
  def get(self, request, format=None):
    model = Software.objects.all()
    serializer = SoftwareSerializer(model,many=True)
    return Response(serializer.data)

class PlantaList(APIView):
  def get(self, request, format=None):
    model = Planta.objects.all()
    serializer = PlantaSerializer(model,many=True)
    return Response(serializer.data)

class EdificioList(APIView):
  def get(self, request, format=None):
    model = Edificio.objects.all()
    serializer = EdificioSerializer(model,many=True)
    return Response(serializer.data)

class Tipo_de_aulaList(APIView):
  def get(self, request, format=None):
    model = Tipo_de_aula.objects.all()
    serializer = Tipo_de_aulaSerializer(model,many=True)
    return Response(serializer.data)

class DiaList(APIView):
  def get(self, request, format=None):
    model = Dia.objects.all()
    serializer = DiaSerializer(model,many=True)
    return Response(serializer.data)

class HoraList(APIView):
  def get(self, request, format=None):
    model = Hora.objects.all()
    serializer = HoraSerializer(model,many=True)
    return Response(serializer.data)

class CarreraList(APIView):
  def get(self, request, format=None):
    model = Carrera.objects.all()
    serializer = CarreraSerializer(model,many=True)
    return Response(serializer.data)

class TurnoList(APIView):
  def get(self, request, format=None):
    model = Turno.objects.all()
    serializer = TurnoSerializer(model,many=True)
    return Response(serializer.data)

class CuatrimestreList(APIView):
  def get(self, request, format=None):
    model = Cuatrimestre.objects.all()
    serializer = CuatrimestreSerializer(model,many=True)
    return Response(serializer.data)

class SolucionList(APIView):
  def get(self, request, format=None):
    model = Solucion.objects.all()
    serializer = SolucionSerializer(model,many=True)
    return Response(serializer.data)

# class List(APIView):
#   def get(self, request, format=None):
#     model = .objects.all()
#     serializer = Serializer(model,many=True)
#     return Response(serializer.data)