from django.conf.urls import include, url
from aula import views
urlpatterns = [
	url(r'^aula/', views.aula),
]
