from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from aula.serializers import *
from aula.models import *
from grupo.serializers import *
from grupo.models import *
from maestro.serializers import *
from maestro.models import *
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
  def post(self, request, format=None):
    serializer = AulaSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AulaDetail(APIView):
  def get_object(self,pk):
    try:
      return Aula.objects.get(pk=pk)
    except Aula.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    aula = self.get_object(pk)
    serializer = AulaSerializer(aula)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    aula = self.get_object(pk)
    serializer = AulaSerializer(aula, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    aula = self.get_object(pk)
    aula.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class Aula_Disponibilidad_List(APIView):
  def post(self, request, pk, format=None):
    serializer = Aula_Disponibilidad_Serializer(data={
      'Id_Disponibilidad':request.POST.get("Id_Disponibilidad")
      ,'Id_Aula':pk
    })
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Aula_Disponibilidad_Detail(APIView):
  def delete(self, request, pk, fk, format=None):
    aula_disponibilidad = Aula_Disponibilidad.objects.filter(Id_Aula=pk,Id_Disponibilidad=fk)
    aula_disponibilidad.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class Aula_Software_List(APIView):
  def post(self, request, pk, format=None):
    serializer = Aula_Software_Serializer(data={
      'Id_Software':request.POST.get('Id_Software')
      ,'Id_Aula':pk
    })
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Aula_Software_Detail(APIView):
  def delete(self, request, pk, fk, format=None):
    aula_software = Aula_Software.objects.filter(Id_Aula=pk,Id_Software=fk)
    aula_software.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class Aula_Materia_List(APIView):
  def post(self, request, pk, format=None):
    serializer = Aula_Materia_Serializer(data={
      'Id_Aula':pk
      ,'Id_Materia':request.POST.get('Id_Materia')
      ,'Horas_Obligatorias':request.POST.get('Horas_Obligatorias')
      ,'Peso':request.POST.get('Peso')
    })
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Aula_Materia_Detail(APIView):
  def delete(self, request, pk, fk, format=None):
    aula_materia = Aula_Materia.objects.filter(Id_Aula=pk, Id_Materia=fk)
    aula_materia.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class GrupoList(APIView):
  def get(self, request, format=None):
    grupo = Grupo.objects.all()
    serializer = GrupoSerializer(grupo,many = True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = GrupoSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GrupoDetail(APIView):
  def get_object(self, pk):
    try:
      return Grupo.objects.get(pk=pk)
    except Grupo.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    grupo = self.get_object(pk)
    serializer = GrupoSerializer(grupo)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    grupo = self.get_object(pk)
    serializer = GrupoSerializer(grupo, data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    grupo = self.get_object(pk)
    grupo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class Grupo_Materia_List(APIView):
  def post(self, request, pk, format=None):
    serializer = Grupo_Materia_Serializer(data={
      'Id_Grupo': pk
      ,'Id_Materia':request.POST.get('Id_Materia')
    })
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MaestroList(APIView):
  def get(self, request, format=None):
    maestro = Maestro.objects.all()
    serializer = MaestroSerializer(maestro, many = True)
    return Response(serializer.data)
  def post(self, request, format=None):
    serializer = MaestroSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MaestroDetail(APIView):
  def get_object(self, pk):
    try:
      return Maestro.objects.get(pk=pk)
    except Maestro.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    maestro = self.get_object(pk)
    serializer = MaestroSerializer(maestro)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    maestro = self.get_object(pk)
    serializer = MaestroSerializer(maestro, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    maestro = self.get_object(pk)
    maestro.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class Maestro_Disponibilidad_List(APIView):
  def post(self, request, pk, format=None):
    serializer= Maestro_Disponibilidad_Serializer(data={
      'Id_Maestro':pk
      ,'Id_Disponibilidad':request.POST.get('Id_Disponibilidad')
    })
    if(serializer.is_valid()):
      serializer.save()
      return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Maestro_Disponibilidad_Detail(APIView):
  def delete(self, request, pk, fk, format=None):
    maestro_disponibilidad = Maestro_Disponibilidad.objects.filter(Id_Maestro=pk, Id_Disponibilidad=fk)
    maestro_disponibilidad.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class Maestro_Materia_List(APIView):
  def post(self, request, pk, format=None):
    serializer= Maestro_Materia_Serializer(data={
      'Id_Maestro':pk
      ,'Id_Materia':request.POST.get('Id_Materia')
    })
    if(serializer.is_valid()):
      serializer.save()
      return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Maestro_Materia_Detail(APIView):
  def delete(self, request, pk, fk, format=None):
    maestro_materia= Maestro_Materia.objects.filter(Id_Maestro=pk, Id_Materia=fk)
    maestro_materia.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class MateriaList(APIView):
  def get(self, request, format=None):
    materia = Materia.objects.all()
    serializer = MateriaSerializer(materia,many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = MateriaSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MateriaDetail(APIView):
  def get_object(self, pk):
    try:
      return Materia.objects.get(pk=pk)
    except Materia.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    materia = self.get_object(pk)
    serializer = MateriaSerializer(materia)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    materia = self.get_object(pk)
    serializer = MateriaSerializer(materia, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
      materia = self.get_object(pk)
      materia.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

class SoftwareList(APIView):
  def get(self, request, format=None):
    model = Software.objects.all()
    serializer = SoftwareSerializer(model,many=True)
    return Response(serializer.data)

class SoftwareDetail(APIView):
  def get_object(self, pk):
    try:
      return Software.objects.get(pk=pk)
    except Software.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    software = self.get_object(pk)
    serializer = SoftwareSerializer(software)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    software = self.get_object(pk)
    serializer = SoftwareSerializer(software, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    software = self.get_object(pk)
    software.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class PlantaList(APIView):
  def get(self, request, format=None):
    model = Planta.objects.all()
    serializer = PlantaSerializer(model,many=True)
    return Response(serializer.data)

class PlantaDetail(APIView):
  def get_object(self, pk):
    try:
      return Planta.objects.get(pk=pk)
    except Planta.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    planta = self.get_object(pk)
    serializer = PlantaSerializer(planta)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    planta = self.get_object(pk)
    serializer = PlantaSerializer(planta, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    planta = self.get_object(pk)
    planta.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class EdificioList(APIView):
  def get(self, request, format=None):
    model = Edificio.objects.all()
    serializer = EdificioSerializer(model,many=True)
    return Response(serializer.data)

class EdificioDetail(APIView):
  def get_object(self, pk):
    try:
      return Edificio.objects.get(pk=pk)
    except Edificio.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    edificio = self.get_object(pk)
    serializer = EdificioSerializer(edificio)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    edificio = self.get_object(pk)
    serializer = EdificioSerializer(edificio, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    edificio = self.get_object(pk)
    edificio.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class Tipo_de_aulaList(APIView):
  def get(self, request, format=None):
    model = Tipo_de_aula.objects.all()
    serializer = Tipo_de_aulaSerializer(model,many=True)
    return Response(serializer.data)

class Tipo_de_aulaDetail(APIView):
  def get_object(self, pk):
    try:
      return Tipo_de_aula.objects.get(pk=pk)
    except Tipo_de_aula.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    tipo_de_aula = self.get_object(pk)
    serializer = Tipo_de_aulaSerializer(tipo_de_aula)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    tipo_de_aula = self.get_object(pk)
    serializer = Tipo_de_aulaSerializer(tipo_de_aula, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    tipo_de_aula = self.get_object(pk)
    tipo_de_aula.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class DiaList(APIView):
  def get(self, request, format=None):
    model = Dia.objects.all()
    serializer = DiaSerializer(model,many=True)
    return Response(serializer.data)

class DiaDetail(APIView):
  def get_object(self, pk):
    try:
      return Dia.objects.get(pk=pk)
    except Dia.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    dia = self.get_object(pk)
    serializer = DiaSerializer(dia)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    dia = self.get_object(pk)
    serializer = DiaSerializer(dia, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    dia = self.get_object(pk)
    dia.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class HoraList(APIView):
  def get(self, request, format=None):
    model = Hora.objects.all()
    serializer = HoraSerializer(model,many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = HoraSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HoraDetail(APIView):
  def get_object(self, pk):
    try:
      return Hora.objects.get(pk=pk)
    except Hora.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    hora = self.get_object(pk)
    serializer = HoraSerializer(hora)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    hora = self.get_object(pk)
    serializer = HoraSerializer(hora, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    hora = self.get_object(pk)
    hora.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class CarreraList(APIView):
  def get(self, request, format=None):
    model = Carrera.objects.all()
    serializer = CarreraSerializer(model,many=True)
    return Response(serializer.data)

class CarreraDetail(APIView):
  def get_object(self, pk):
    try:
      return Carrera.objects.get(pk=pk)
    except Carrera.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    carrera = self.get_object(pk)
    serializer = CarreraSerializer(carrera)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    carrera = self.get_object(pk)
    serializer = CarreraSerializer(carrera, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    carrera = self.get_object(pk)
    carrera.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class TurnoList(APIView):
  def get(self, request, format=None):
    model = Turno.objects.all()
    serializer = TurnoSerializer(model,many=True)
    return Response(serializer.data)

class TurnoDetail(APIView):
  def get_object(self, pk):
    try:
      return Turno.objects.get(pk=pk)
    except Turno.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    turno = self.get_object(pk)
    serializer = TurnoSerializer(turno)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    turno = self.get_object(pk)
    serializer = TurnoSerializer(turno, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    turno = self.get_object(pk)
    turno.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class DisponibilidadList(APIView):
  def get(self, request, format=None):
    model = Disponibilidad.objects.all()
    serializer = DisponibilidadSerializer(model,many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = DisponibilidadSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DisponibilidadDetail(APIView):
  def get_object(self, pk):
    try:
      return Disponibilidad.objects.get(pk=pk)
    except Disponibilidad.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    disponibilidad = self.get_object(pk)
    serializer = DisponibilidadSerializer(disponibilidad)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    disponibilidad = self.get_object(pk)
    serializer = DisponibilidadSerializer(disponibilidad, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    disponibilidad = self.get_object(pk)
    disponibilidad.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class CuatrimestreList(APIView):
  def get(self, request, format=None):
    model = Cuatrimestre.objects.all()
    serializer = CuatrimestreSerializer(model,many=True)
    return Response(serializer.data)

class CuatrimestreDetail(APIView):
  def get_object(self, pk):
    try:
      return Cuatrimestre.objects.get(pk=pk)
    except Cuatrimestre.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    cuatrimestre = self.get_object(pk)
    serializer = CuatrimestreSerializer(cuatrimestre)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    cuatrimestre = self.get_object(pk)
    serializer = CuatrimestreSerializer(cuatrimestre, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    cuatrimestre = self.get_object(pk)
    cuatrimestre.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class SolucionList(APIView):
  def get(self, request, format=None):
    model = Solucion.objects.all()
    serializer = SolucionSerializer(model,many=True)
    return Response(serializer.data)

class SolucionDetail(APIView):
  def get_object(self, pk):
    try:
      return Solucion.objects.get(pk=pk)
    except Solucion.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    solucion = self.get_object(pk)
    serializer = SolucionSerializer(solucion)
    return Response(serializer.data)

  def put(self, request, pk, format=None):
    solucion = self.get_object(pk)
    serializer = SolucionSerializer(solucion, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
    solucion = self.get_object(pk)
    solucion.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
