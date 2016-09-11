from django.conf.urls import include, url
from materia import views
urlpatterns = [
	url(r'^$', views.materia),
	url(r'^getdata_json$', views.myajaxview, name='getdata_json'),
]
