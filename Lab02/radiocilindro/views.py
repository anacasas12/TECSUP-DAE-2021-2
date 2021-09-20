from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'formulario.html')

def respuesta(request):
    diametro = request.POST['diametro']
    altura =request.POST['altura']
    respuesta = 3.14159265358979323846*float(diametro)*float(altura)
    context={
       'resultado' :  respuesta ,
         'diametro': diametro,
       'altura' : altura
    }
    return  render(request,'respuesta.html',context)