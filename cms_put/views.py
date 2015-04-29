from django.shortcuts import render
from models import Pages
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context

# Create your views here.

@csrf_exempt
def mostrar(request, recurso):
	if request.method == "GET":
		#MUESTRO DE LA BD
		try:
			fila = Pages.objects.get(name=recurso)
			
			plantilla = get_template('index.html')
			c = Context({'title': recurso, 'contenido': fila.page, 'user': request.user.username,})
			renderizado = plantilla.render(c)
			
			return HttpResponse(renderizado)
		except Pages.DoesNotExist:
			return HttpResponseNotFound("Page not found: " + recurso)
	elif request.method == "PUT":
		#GUARDO EN LA BD
		try:
			p = Pages.objects.get(name=recurso)
			p.page = request.body
		except Pages.DoesNotExist:
			p = Pages(name=recurso, page=request.body)
		p.save()
		return HttpResponse("guardada pagina, haz un get para comprobar")

@csrf_exempt		
def css(request, recurso):
	if request.method == "GET":
		#MUESTRO DE LA BD
		try:
			fila = Pages.objects.get(name=recurso)			
			return HttpResponse(fila.page, content_type="text/css")
		except Pages.DoesNotExist:
			return HttpResponseNotFound("CSS not found: " + recurso)
	elif request.method == "PUT":
		#GUARDO EN LA BD
		try:
			p = Pages.objects.get(name=recurso)
			p.page = request.body
		except Pages.DoesNotExist:
			p = Pages(name=recurso, page=request.body)
		p.save()
		return HttpResponse("guardada pagina, haz un get para comprobar")	
