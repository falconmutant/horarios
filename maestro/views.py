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
    response_data['Nombre'] = maestro.Nombre+" "+maestro.Apellido_Paterno+" "+maestro.Apellido_Materno
    response_data['Modificar'] = '<a href=""><i class="fa fa-book" aria-hidden="true"></i></a>'
    response_data['Eliminar'] = '<a href=""><i class="fa fa-trash" aria-hidden="true"></i></a>'
    response_data['Disponibilidad'] = '<a href=""><i class="fa fa-cubes" aria-hidden="true"></i></a>'
    response_data['Materia'] = '<a href=""><i class="fa fa-tasks" aria-hidden="true"></i></a>'
    response_data['Software'] = '<a href=""><i class="fa fa-cubes" aria-hidden="true"></i></a>'
    report.append(response_data)
  data = json.dumps(report)
  return HttpResponse(data, content_type='application/json')
