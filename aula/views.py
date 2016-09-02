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
def aula(request):
	user_name = request.user.username
	aula_tipo = Tipo_de_aula.objects.all()
	edificio = Edificio.objects.all()
	planta = Planta.objects.all()
	horas = Hora.objects.all()
	dias = Dia.objects.all()
	cursor = connection.cursor()
	cursor.execute("select dia.id as Id_Dia, hora.id as Id_Hora from (modulos_dia dia,modulos_hora hora) left join modulos_disponibilidad disp on dia.id=disp.Id_Dia_id and hora.id = disp.Id_Hora_id where disp.Id_Hora_id is null order by Id_Dia,Id_hora")
	horas_no_disponibles = dictfetchall(cursor)
	aula_disponibilidad = Aula_Disponibilidad.objects.all()
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
		response_data['Modificar'] = '<a href="" data-toggle="modal" id="modificar" data-target="#modificar"><i class="fa fa-book" aria-hidden="true"></i></a>'
		response_data['Eliminar'] = '<a href=""><i class="fa fa-trash" aria-hidden="true"></i></a>'
		response_data['Disponibilidad'] = '<a href="" data-toggle="modal" data-target="#disponibilidad"><i class="fa fa-cubes" aria-hidden="true"></i></a>'
		response_data['Materia'] = '<a href=""><i class="fa fa-tasks" aria-hidden="true"></i></a>'
		response_data['Software'] = '<a href=""><i class="fa fa-cubes" aria-hidden="true"></i></a>'
		report.append(response_data)
	data = json.dumps(report)
	return HttpResponse(data, content_type='application/json')

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]