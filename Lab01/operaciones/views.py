from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def suma(request,a,b):
    respuesta=a+b
    return HttpResponse("La suma de "+str(a)+" + "+str(b)+" = "+str(respuesta))
def resta(request,a,b):
    respuesta=a-b
    return HttpResponse("La resta de "+str(a)+" - "+str(b)+" = "+str(respuesta))
def multiplicacion(request,a,b):
    respuesta=a*b
    return HttpResponse("La multiplicacion de "+str(a)+" x "+str(b)+" = "+str(respuesta))
def division(request,a,b):    
     respuesta=a/b
     return HttpResponse("La division de "+str(a)+" / "+str(b)+" = "+str(respuesta))