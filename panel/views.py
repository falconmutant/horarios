from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from aula.models import Aula
from materia.models import Materia
from grupo.models import Grupo
from maestro.models import Maestro
from modulos.models import *
# Create your views here.

def index(request):
	return HttpResponseRedirect('/Dashboard/')

@login_required
def logged_in(request):
	user_name = request.user.username
	aula_count = Aula.objects.all().count()
	materia_count = Materia.objects.all().count()
	grupo_count = Grupo.objects.all().count()
	maestro_count = Maestro.objects.all().count()
	return render_to_response('dashboard.html',RequestContext(request,locals()))

@login_required
def disponibilidad(request):
	horas = Hora.objects.all()
	dias = Dia.objects.all()
	return render(request, "disponibilidad.html", locals())