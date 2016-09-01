from django.conf.urls import include, url
from api import views
urlpatterns = [
  url(r'^aula/$', views.AulaList.as_view()),
  url(r'^grupo/$', views.GrupoList.as_view()),
  url(r'^maestro/$', views.MaestroList.as_view()),
  url(r'^materia/$', views.MateriaList.as_view()),
  url(r'^software/$', views.SoftwareList.as_view()),
  url(r'^planta/$', views.PlantaList.as_view()),
  url(r'^edificio/$', views.EdificioList.as_view()),
  url(r'^tipoAula/$', views.Tipo_de_aulaList.as_view()),
  url(r'^dia/$', views.DiaList.as_view()),
  url(r'^hora/$', views.HoraList.as_view()),
  url(r'^carrera/$', views.CarreraList.as_view()),
  url(r'^turno/$', views.TurnoList.as_view()),
  url(r'^cuatrimestre/$', views.CuatrimestreList.as_view()),
  url(r'^solucion/$', views.SolucionList.as_view()),
]