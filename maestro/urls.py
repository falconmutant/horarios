from django.conf.urls import include, url
from maestro import views
urlpatterns = [
  url(r'^$', views.maestro),
  url(r'^getdata_json$', views.myajaxview, name='getdata_json'),
]
