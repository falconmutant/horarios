from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

# Create your views here.
@login_required
def aula(request):
	user_name = request.user.username
	return render_to_response('aula/aula.html',RequestContext(request,locals()))