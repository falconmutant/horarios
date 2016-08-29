from django.conf.urls import include, url
from maestro import views
urlpatterns = [
  url(r'^maestro/', views.index),
]
