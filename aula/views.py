import json
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from modulos.models import *
from .models import *

# Create your views here.
@login_required
def aula(request):
	user_name = request.user.username
	aula_tipo = Tipo_de_aula.objects.all()
	edificio = Edificio.objects.all()
	planta = Planta.objects.all()
	if request.POST:
		id_planta = Planta.objects.get(id=request.POST["planta"])
		id_edificio = Edificio.objects.get(id=request.POST["edificio"])
		plantaedificio = Planta_edificio(Id_Planta=id_planta,Id_Edificio=id_edificio)
		plantaedificio.save()
		tipo_aula = Tipo_de_aula.objects.get(id=request.POST["tipo"])
		aula = Aula(Nombre = request.POST["nombre"],Capacidad = request.POST["capacidad"],
			Id_Tipo_de_aula = tipo_aula,Id_Planta_Edificio = plantaedificio)
		aula.save()
		mensaje=1
	return render(request, "aula/aula.html", locals())

def myajaxview(request):
	report = []
	aulas = Aula.objects.all()
	for nombre in aulas:
		response_data = {}
		response_data['Aula'] = nombre.Nombre
		response_data['Modificar'] = '<a href=""><i class="fa fa-book" aria-hidden="true"></i></a>'
		response_data['Eliminar'] = '<a href=""><i class="fa fa-trash" aria-hidden="true"></i></a>'
		response_data['Disponibilidad'] = '<a href=""><i class="fa fa-cubes" aria-hidden="true"></i></a>'
		response_data['Materia'] = '<a href=""><i class="fa fa-tasks" aria-hidden="true"></i></a>'
		response_data['Software'] = '<a href=""><i class="fa fa-cubes" aria-hidden="true"></i></a>'
		report.append(response_data)
	data = json.dumps(report)
	return HttpResponse(data, content_type='application/json')