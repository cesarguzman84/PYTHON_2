from django.http import HttpResponse

def Bienvenida(request):
	return HttpResponse("Bienvenido a este curso")

def BienvenidaRojo(request):
	return HttpResponse("Bienvenido a este curso de Django Prueba")

