from typing import ContextManager
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'formulario.html')
def enviar(request):
    num1 = request.POST['num1']
    num2 = request.POST['num2']
    operacion = request.POST['operacion']
    if operacion=='suma':
        resultado=int(num1)+int(num2)
    elif operacion=='resta':
        resultado=int(num1)-int(num2)
    elif operacion=='multiplicacion':
        resultado=int(num1)*int(num2)
    else :
        resultado= int(num1)/int(num2)

    context = {
        'titulo' : "Respuesta de la operacion",
        'num1' : num1,
        'num2': num2,
        'respuesta' : resultado,
        'operacion': operacion
    }
    return render(request,'respuesta.html',context)