from django.conf.urls import include, url
from api import views
urlpatterns = [
  url(r'^aula/$', views.AulaList.as_view()),
  url(r'^aula/(?P<pk>[0-9]+)/$', views.AulaDetail.as_view()),
  url(r'^aula/(?P<pk>[0-9]+)/disponibilidad/$', views.Aula_Disponibilidad.as_view()),
  url(r'^aula/(?P<pk>[0-9]+)/software/$', views.Aula_Software.as_view()),
  url(r'^aula/(?P<pk>[0-9]+)/materia/$', views.Aula_Materia.as_view()),
  url(r'^grupo/$', views.GrupoList.as_view()),
  url(r'^grupo/(?P<pk>[0-9]+)/$', views.GrupoDetail.as_view()),
  url(r'^maestro/$', views.MaestroList.as_view()),
  url(r'^maestro/(?P<pk>[0-9]+)/$', views.MaestroDetail.as_view()),
  url(r'^maestro/(?P<pk>[0-9]+)/disponibilidad/$', views.Maestro_Disponibilidad_List.as_view()),
  url(r'^maestro/(?P<pk>[0-9]+)/materia/$', views.Maestro_Materia_List.as_view()),
  url(r'^materia/$', views.MateriaList.as_view()),
  url(r'^materia/(?P<pk>[0-9]+)/$', views.MateriaDetail.as_view()),
  url(r'^software/$', views.SoftwareList.as_view()),
  url(r'^software/(?P<pk>[0-9]+)/$', views.SoftwareDetail.as_view()),
  url(r'^planta/$', views.PlantaList.as_view()),
  url(r'^planta/(?P<pk>[0-9]+)/$', views.PlantaDetail.as_view()),
  url(r'^edificio/$', views.EdificioList.as_view()),
  url(r'^edificio/(?P<pk>[0-9]+)/$', views.EdificioDetail.as_view()),
  url(r'^tipoAula/$', views.Tipo_de_aulaList.as_view()),
  url(r'^tipoAula/(?P<pk>[0-9]+)/$', views.Tipo_de_aulaDetail.as_view()),
  url(r'^dia/$', views.DiaList.as_view()),
  url(r'^dia/(?P<pk>[0-9]+)/$', views.DiaDetail.as_view()),
  url(r'^hora/$', views.HoraList.as_view()),
  url(r'^hora/(?P<pk>[0-9]+)/$', views.HoraDetail.as_view()),
  url(r'^carrera/$', views.CarreraList.as_view()),
  url(r'^carrera/(?P<pk>[0-9]+)/$', views.CarreraDetail.as_view()),
  url(r'^turno/$', views.TurnoList.as_view()),
  url(r'^turno/(?P<pk>[0-9]+)/$', views.TurnoDetail.as_view()),
  url(r'^disponibilidad/$', views.DisponibilidadList.as_view()),
  url(r'^disponibilidad/(?P<pk>[0-9]+)/$', views.DisponibilidadDetail.as_view()),
  url(r'^cuatrimestre/$', views.CuatrimestreList.as_view()),
  url(r'^cuatrimestre/(?P<pk>[0-9]+)/$', views.CuatrimestreDetail.as_view()),
  url(r'^solucion/$', views.SolucionList.as_view()),
  url(r'^solucion/(?P<pk>[0-9]+)/$', views.SolucionDetail.as_view()),
]
