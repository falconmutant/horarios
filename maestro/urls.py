from django.conf.urls import include, url
from maestro import views
urlpatterns = [
  url(r'^$', views.index),
  url(r'^datatable$', views.datatable, name='datatable'),
]
