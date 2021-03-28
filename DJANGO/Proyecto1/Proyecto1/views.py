from django.http import HttpResponse
import datetime

def saludo(request):  #Primera vista

    documento= "<html><body><h1>Hola alumnos, esta es nuestra primera pagina con django</h1></body></html>"
    
    return HttpResponse (documento)

def despedida(request):

    return HttpResponse ("Hasta luego alumnos django")

def dameFecha(request):

    fecha_actual = datetime.datetime.now()

    
    documento='''<html>
    <body>
    <h1>
    Fecha y hora actuales %
    </h1>
    </body>
    </html>''' % fecha_actual

    return HttpResponse (documento)