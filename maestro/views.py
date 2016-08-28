from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

# Create your views here.
@login_required
def new(request):
	user_name = request.user.username
	return render_to_response('maestro/new.html',RequestContext(request,locals()))
