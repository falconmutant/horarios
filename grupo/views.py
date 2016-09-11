import json
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from modulos.models import *
from .models import *
from django.db import connection


# Create your views here.
@login_required
def grupo(request):
	user_name = request.user.username
	turnos = Turno.objects.all()
	tipo = TIPO
	materias = Materia.objects.all()
	if request.POST:
		if 'id_grupo' not in request.POST:
			turno = Turno.objects.get(id=request.POST["turno"])
			grupo = Grupo(Nombre=request.POST["nombre"],Tipo_Grupo=request.POST["tipo"],Id_Turno=turno)
			grupo.save()
			mensaje=1
		else:
			turno = Turno.objects.get(id=request.POST["turno"])
			Grupo.objects.filter(id=request.POST["id_grupo"]).update(Nombre=request.POST["nombre"],
				Tipo_Grupo=request.POST["tipo"],Id_Turno=turno)
			mensaje=2
	return render(request, "grupo/grupo.html", locals())

def myajaxview(request):
	report = []
	grupos = Grupo.objects.all()
	for grupo in grupos:
		response_data = {}
		response_data['Nombre'] = grupo.Nombre
		response_data['Modificar'] = '<a href="" onclick="modificar('+str(grupo.id)+');" data-toggle="modal" data-target="#modificar"><i class="fa fa-book" aria-hidden="true"></i></a>'
		response_data['Eliminar'] = '<a href="" onclick="setidgrupo('+str(grupo.id)+');" data-toggle="modal" data-target="#eliminar"><i class="fa fa-trash" aria-hidden="true"></i></a>'
		response_data['Materia'] = '<a href="" onclick="materia('+str(grupo.id)+');" data-toggle="modal" data-target="#materia"><i class="fa fa-tasks" aria-hidden="true"></i></a>'
		report.append(response_data)
	data = json.dumps(report)
	return HttpResponse(data, content_type='application/json')