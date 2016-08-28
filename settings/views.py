from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
# Create your views here.

def index(request):
	return HttpResponseRedirect('/Dashboard/')

@login_required
def logged_in(request):
	user_name = request.user.username
	return render_to_response('dashboard.html',RequestContext(request,locals()))