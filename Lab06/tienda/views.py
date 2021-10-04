from django.shortcuts import get_object_or_404, render

from .models import Categoria, Producto
# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    category_list = Categoria.objects.order_by('nombre')[:4]
    context = {
        'product_list':product_list,
        'category_list':category_list
    }
    return render(request,'index.html',context)

def categoria(request, categoria_id):
    categoria=get_object_or_404(Categoria,pk=categoria_id)
    return render(request, 'categoria.html',{'categoria':categoria})