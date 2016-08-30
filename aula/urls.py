from django.conf.urls import include, url
from aula import views
urlpatterns = [
	url(r'^$', views.aula),
	url(r'^getdata_json$', views.myajaxview, name='getdata_json')
]
