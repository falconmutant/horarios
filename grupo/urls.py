from django.conf.urls import include, url
from grupo import views
urlpatterns = [
	url(r'^$', views.grupo),
	url(r'^getdata_json$', views.myajaxview, name='getdata_json'),
]
