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
def materia(request):
	user_name = request.user.username
	carreras = Carrera.objects.all()
	if request.POST:
		if 'id_materia' not in request.POST:
			cuatri = Cuatrimestre.objects.get(Id_Carrera=request.POST["carrera"],Cuatrimestre=request.POST["cuatrimestre"])
			materia = Materia(Nombre=request.POST["nombre"],Horas_Por_Semana=request.POST["horas"],Id_Cuatrimestre=cuatri)
			materia.save()
			mensaje=1
		else:
			cuatri = Cuatrimestre.objects.get(Id_Carrera=request.POST["carrera"],Cuatrimestre=request.POST["cuatrimestre"])
			Materia.objects.filter(id=request.POST["id_materia"]).update(Nombre=request.POST["nombre"],
				Horas_Por_Semana=request.POST["horas"],Id_Cuatrimestre=cuatri)
			mensaje=2
	return render(request, "materia/materia.html", locals())

def myajaxview(request):
	report = []
	materias = Materia.objects.all()
	for materia in materias:
		response_data = {}
		response_data['Nombre'] = materia.Nombre
		response_data['Modificar'] = '<a href="" onclick="modificar('+str(materia.id)+');" data-toggle="modal" data-target="#modificar"><i class="fa fa-book" aria-hidden="true"></i></a>'
		response_data['Eliminar'] = '<a href="" onclick="setidmateria('+str(materia.id)+');" data-toggle="modal" data-target="#eliminar"><i class="fa fa-trash" aria-hidden="true"></i></a>'
		report.append(response_data)
	data = json.dumps(report)
	return HttpResponse(data, content_type='application/json')