from django.shortcuts import render, render_to_response, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import JsonResponse,HttpResponse
from .models import Maestro
import json

# Create your views here.

def index(request):
  user_name = request.user.username
  return render_to_response('maestro/index.html',RequestContext(request,locals()))

def datatable(request):
  report = []
  maestros = Maestro.objects.all()
  for maestro in maestros:
    response_data = {}
    response_data['Nombre'] = maestro.Nombre
    response_data['Apellido_Paterno'] = maestro.Apellido_Paterno
    response_data['Apellido_Materno'] = maestro.Apellido_Materno
    response_data['Contrato'] = maestro.Contrato
    response_data['Proyecto_Financiado'] = maestro.Proyecto_Financiado
    response_data['Grado_De_Estudio'] = maestro.Grado_De_Estudio
    response_data['Clase_Maestria'] = maestro.Clase_Maestria
    response_data['Num_Materias'] = maestro.Num_Materias
    report.append(response_data)
  data = json.dumps(report)
  return HttpResponse(data, content_type='application/json')
