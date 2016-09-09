from django.conf.urls import include, url
from modulos import views
urlpatterns = [
  url(r'^$', views.index)
  ,url(r'^carrera$', views.carrera)
  ,url(r'^cuatrimestre$', views.cuatrimestre)
  ,url(r'^edificio$', views.edificio)
  ,url(r'^planta$', views.planta)
  ,url(r'^planta_edificio$', views.planta_edificio)
  ,url(r'^software$', views.software)
  ,url(r'^dia$', views.dia)
  ,url(r'^hora$', views.hora)
]
