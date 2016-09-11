import json
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from modulos.models import *
from .models import *

# Create your views here.
@login_required
def maestro(request):
  user_name = request.user.username
  contrato = CONTRATO
  proyecto = FINANCIADO
  maestria = SI_NO
  grado = GRADO
  horas = Hora.objects.all()
  dias = Dia.objects.all()
  materias = Materia.objects.all()
  if request.POST:
    if 'id_maestro' not in request.POST:
      maestro = Maestro(Nombre = request.POST["nombre"],Apellido_Paterno = request.POST["paterno"],Apellido_Materno = request.POST["materno"],
        Contrato = request.POST["contrato"],Proyecto_Financiado = request.POST["proyecto"],Grado_De_Estudio = request.POST["grado"],
        Clase_Maestria = request.POST["maestria"],Num_Materias = request.POST["materias"])
      maestro.save()
      mensaje=1
    else:
      Maestro.objects.filter(id=request.POST["id_maestro"]).update(Nombre = request.POST["nombre"],Apellido_Paterno = request.POST["paterno"],Apellido_Materno = request.POST["materno"],
        Contrato = request.POST["contrato"],Proyecto_Financiado = request.POST["proyecto"],Grado_De_Estudio = request.POST["grado"],
        Clase_Maestria = request.POST["maestria"],Num_Materias = request.POST["materias"])
      mensaje=2
  return render(request, "maestro/maestro.html", locals())

def myajaxview(request):
  report = []
  maestros = Maestro.objects.all()
  for maestro in maestros:
    response_data = {}
    response_data['Nombre'] = maestro.Nombre+" "+maestro.Apellido_Paterno+" "+maestro.Apellido_Materno
    response_data['Modificar'] = '<a href="" onclick="modificar('+str(maestro.id)+');" data-toggle="modal" data-target="#modificar"><i class="fa fa-book" aria-hidden="true"></i></a>'
    response_data['Eliminar'] = '<a href="" onclick="setidmaestro('+str(maestro.id)+');" data-toggle="modal" data-target="#eliminar"><i class="fa fa-trash" aria-hidden="true"></i></a>'
    response_data['Disponibilidad'] = '<a href=""  onclick="cargar('+str(maestro.id)+');" data-toggle="modal" data-target="#disponibilidad"><i class="fa fa-cubes" aria-hidden="true"></i></a>'
    response_data['Materia'] = '<a href="" onclick="materia('+str(maestro.id)+');" data-toggle="modal" data-target="#materia"><i class="fa fa-tasks" aria-hidden="true"></i></a>'
    report.append(response_data)
  data = json.dumps(report)
  return HttpResponse(data, content_type='application/json')
