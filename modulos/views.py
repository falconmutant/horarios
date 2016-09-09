from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, "modulos/index.html", locals())

def carrera(request):
  return render(request, "modulos/carrera.html", locals())

def cuatrimestre(request):
  return render(request, "modulos/cuatrimestre.html", locals())

def edificio(request):
  return render(request, "modulos/edificio.html", locals())

def planta(request):
  return render(request, "modulos/planta.html", locals())

def planta_edificio(request):
  return render(request, "modulos/planta_edificio.html", locals())

def software(request):
  return render(request, "modulos/software.html", locals())

def dia(request):
  return render(request, "modulos/dia.html", locals())

def hora(request):
  return render(request, "modulos/hora.html", locals())
