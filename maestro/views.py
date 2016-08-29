from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import JsonResponse

# Create your views here.

def index(request):
  user_name = request.user.username
  return render_to_response('maestro/index.html',RequestContext(request,locals()))

def datatable(request):
  # return JsonResponse({'foo':'bar'})
  return render_to_response('blblbl')
