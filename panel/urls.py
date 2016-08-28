from django.conf.urls import include, url
from panel import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
urlpatterns = [
	url(r'^$', views.index),
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'login.html'}, name='logout'),
	url(r'^Dashboard/', views.logged_in),
]
