from django.conf.urls import include, url
from modulos import views
urlpatterns = [
  url(r'^$', views.index)
  ,url(r'^carrera$', views.carrera)
  ,url(r'^carrera/getdata_json$', views.carrera_myajaxview, name='getdata_json')
  ,url(r'^cuatrimestre$', views.cuatrimestre)
  ,url(r'^cuatrimestre/getdata_json$', views.cuatrimestre_myajaxview, name='getdata_json')
  ,url(r'^edificio$', views.edificio)
  ,url(r'^edificio/getdata_json$', views.edificio_myajaxview, name='getdata_json')
  ,url(r'^planta$', views.planta)
  ,url(r'^planta/getdata_json$', views.planta_myajaxview, name='getdata_json')
  ,url(r'^planta_edificio$', views.planta_edificio)
  ,url(r'^planta_edificio/getdata_json$', views.planta_edificio_myajaxview, name='getdata_json')
  ,url(r'^software$', views.software)
  ,url(r'^software/getdata_json$', views.software_myajaxview, name='getdata_json')
  ,url(r'^dia$', views.dia)
  ,url(r'^dia/getdata_json$', views.dia_myajaxview, name='getdata_json')
  ,url(r'^hora$', views.hora)
  ,url(r'^hora/getdata_json$', views.hora_myajaxview, name='getdata_json')
]
