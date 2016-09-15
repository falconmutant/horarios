import json
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .models import *
from django.db import connection

# Create your views here.
def index(request):
	return render(request, "modulos/index.html", locals())

def carrera(request):
	user_name = request.user.username
	if request.POST:
		if 'id_carrera' not in request.POST:
			carrera = Carrera(Carrera=request.POST['nombre'])
			carrera.save()
			mensaje=1
		else:
			Carrera.objects.filter(id=request.POST['id_carrera']).update(Carrera=request.POST['nombre'])
			mensaje=2
	return render(request, "modulos/carrera.html", locals())

def carrera_myajaxview(request):
	report = []
	carreras = Carrera.objects.all()
	for carrera in carreras:
		response_data = {}
		response_data['Carrera'] = carrera.Carrera
		response_data['Modificar'] = '<a href="" onclick="modificar('+str(carrera.id)+');" data-toggle="modal" data-target="#modificar"><i class="fa fa-book" aria-hidden="true"></i></a>'
		response_data['Eliminar'] = '<a href="" onclick="setidcarrera('+str(carrera.id)+');" data-toggle="modal" data-target="#eliminar"><i class="fa fa-trash" aria-hidden="true"></i></a>'
		report.append(response_data)
	data = json.dumps(report)
	return HttpResponse(data, content_type='application/json')

def cuatrimestre(request):
	user_name = request.user.username
	carreras = Carrera.objects.all()
	if request.POST:
		if 'id_cuatrimestre' not in request.POST:
			carrera = Carrera.objects.get(id=request.POST['carrera'])
			cuatrimestre = Cuatrimestre(Cuatrimestre=request.POST['cuatrimestre'],Id_Carrera=carrera)
			cuatrimestre.save()
			mensaje=1
		else:
			carrera = Carrera.objects.get(id=request.POST['carrera'])
			Cuatrimestre.objects.filter(id=request.POST['id_cuatrimestre']).update(Cuatrimestre=request.POST['cuatrimestre'],Id_Carrera=carrera)
			mensaje=2
	return render(request, "modulos/cuatrimestre.html", locals())

def cuatrimestre_myajaxview(request):
	report = []
	cuatrimestres = Cuatrimestre.objects.all()
	for cuatrimestre in cuatrimestres:
		response_data = {}
		carrera = Carrera.objects.get(id=cuatrimestre.Id_Carrera_id)
		response_data['Carrera'] = carrera.Carrera
		response_data['Cuatrimestre'] = cuatrimestre.Cuatrimestre
		response_data['Modificar'] = '<a href="" onclick="modificar('+str(cuatrimestre.id)+');" data-toggle="modal" data-target="#modificar"><i class="fa fa-book" aria-hidden="true"></i></a>'
		response_data['Eliminar'] = '<a href="" onclick="setidcuatrimestre('+str(cuatrimestre.id)+');" data-toggle="modal" data-target="#eliminar"><i class="fa fa-trash" aria-hidden="true"></i></a>'
		report.append(response_data)
	data = json.dumps(report)
	return HttpResponse(data, content_type='application/json')

def edificio(request):
	user_name = request.user.username
	if request.POST:
		if 'id_edificio' not in request.POST:
			edificio = Edificio(Nombre_Edificio=request.POST['nombre'])
			edificio.save()
			mensaje=1
		else:
			Edificio.objects.filter(id=request.POST["id_edificio"]).update(Nombre_Edificio=request.POST['nombre'])
			mensaje=2
	return render(request, "modulos/edificio.html", locals())

def edificio_myajaxview(request):
	report = []
	edificios = Edificio.objects.all()
	for edificio in edificios:
		response_data = {}
		response_data['Edificio'] = edificio.Nombre_Edificio
		response_data['Modificar'] = '<a href="" onclick="modificar('+str(edificio.id)+');" data-toggle="modal" data-target="#modificar"><i class="fa fa-book" aria-hidden="true"></i></a>'
		response_data['Eliminar'] = '<a href="" onclick="setidedificio('+str(edificio.id)+');" data-toggle="modal" data-target="#eliminar"><i class="fa fa-trash" aria-hidden="true"></i></a>'
		report.append(response_data)
	data = json.dumps(report)
	return HttpResponse(data, content_type='application/json')

def planta(request):
	user_name = request.user.username
	if request.POST:
		if 'id_planta' not in request.POST:
			planta = Planta(Planta=request.POST['nombre'])
			planta.save()
			mensaje=1
		else:
			Planta.objects.filter(id=request.POST["id_planta"]).update(Planta=request.POST['nombre'])
			mensaje=2
	return render(request, "modulos/planta.html", locals())

def planta_myajaxview(request):
	report = []
	plantas = Planta.objects.all()
	for planta in plantas:
		response_data = {}
		response_data['Planta'] = planta.Planta
		response_data['Modificar'] = '<a href="" onclick="modificar('+str(planta.id)+');" data-toggle="modal" data-target="#modificar"><i class="fa fa-book" aria-hidden="true"></i></a>'
		response_data['Eliminar'] = '<a href="" onclick="setidplanta('+str(planta.id)+');" data-toggle="modal" data-target="#eliminar"><i class="fa fa-trash" aria-hidden="true"></i></a>'
		report.append(response_data)
	data = json.dumps(report)
	return HttpResponse(data, content_type='application/json')

def planta_edificio(request):
	return render(request, "modulos/planta_edificio.html", locals())

def planta_edificio_myajaxview(request):
	report = []
	softwares = Software.objects.all()
	for software in softwares:
		response_data = {}
		response_data['Software'] = software.Nombre
		response_data['Modificar'] = '<a href="" onclick="modificar('+str(software.id)+');" data-toggle="modal" data-target="#modificar"><i class="fa fa-book" aria-hidden="true"></i></a>'
		response_data['Eliminar'] = '<a href="" onclick="setidmateria('+str(software.id)+');" data-toggle="modal" data-target="#eliminar"><i class="fa fa-trash" aria-hidden="true"></i></a>'
		report.append(response_data)
	data = json.dumps(report)
	return HttpResponse(data, content_type='application/json')


def software(request):
	user_name = request.user.username
	if request.POST:
		if 'id_software' not in request.POST:
			software = Software(Nombre=request.POST['nombre'])
			software.save()
			mensaje=1
		else:
			Software.objects.filter(id=request.POST["id_software"]).update(Nombre=request.POST['nombre'])
			mensaje=2
	return render(request, "modulos/software.html", locals())

def software_myajaxview(request):
	report = []
	softwares = Software.objects.all()
	for software in softwares:
		response_data = {}
		response_data['Software'] = software.Nombre
		response_data['Modificar'] = '<a href="" onclick="modificar('+str(software.id)+');" data-toggle="modal" data-target="#modificar"><i class="fa fa-book" aria-hidden="true"></i></a>'
		response_data['Eliminar'] = '<a href="" onclick="setidsoftware('+str(software.id)+');" data-toggle="modal" data-target="#eliminar"><i class="fa fa-trash" aria-hidden="true"></i></a>'
		report.append(response_data)
	data = json.dumps(report)
	return HttpResponse(data, content_type='application/json')

def dia(request):
	user_name = request.user.username
	if request.POST:
		if 'id_dia' not in request.POST:
			dia = Dia(Dia=request.POST['nombre'])
			dia.save()
			mensaje=1
		else:
			Dia.objects.filter(id=request.POST["id_dia"]).update(Dia=request.POST['nombre'])
			mensaje=2
	return render(request, "modulos/dia.html", locals())

def dia_myajaxview(request):
	report = []
	dias = Dia.objects.all()
	for dia in dias:
		response_data = {}
		response_data['Dia'] = dia.Dia
		response_data['Modificar'] = '<a href="" onclick="modificar('+str(dia.id)+');" data-toggle="modal" data-target="#modificar"><i class="fa fa-book" aria-hidden="true"></i></a>'
		response_data['Eliminar'] = '<a href="" onclick="setiddia('+str(dia.id)+');" data-toggle="modal" data-target="#eliminar"><i class="fa fa-trash" aria-hidden="true"></i></a>'
		report.append(response_data)
	data = json.dumps(report)
	return HttpResponse(data, content_type='application/json')

def hora(request):
	user_name = request.user.username
	if request.POST:
		if 'id_hora' not in request.POST:
			hora = Hora(Hora=request.POST['nombre'])
			hora.save()
			mensaje=1
		else:
			Hora.objects.filter(id=request.POST["id_hora"]).update(Hora=request.POST['nombre'])
			mensaje=2
	return render(request, "modulos/hora.html", locals())

def hora_myajaxview(request):
	report = []
	horas = Hora.objects.all()
	for hora in horas:
		response_data = {}
		response_data['Hora'] = hora.Hora
		response_data['Modificar'] = '<a href="" onclick="modificar('+str(hora.id)+');" data-toggle="modal" data-target="#modificar"><i class="fa fa-book" aria-hidden="true"></i></a>'
		response_data['Eliminar'] = '<a href="" onclick="setidhora('+str(hora.id)+');" data-toggle="modal" data-target="#eliminar"><i class="fa fa-trash" aria-hidden="true"></i></a>'
		report.append(response_data)
	data = json.dumps(report)
	return HttpResponse(data, content_type='application/json')
