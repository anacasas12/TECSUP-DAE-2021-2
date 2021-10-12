from django.shortcuts import get_object_or_404, render

from .models import Categoria, Producto
# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    category_list = Categoria.objects.all()

    dicCategorias={}
    for cat in category_list:
        dicCategorias[cat.id]={
            'id':cat.id,
            'nombre':cat.nombre
        }

    request.session['nombreTienda']='SuperMarket'
    request.session['listado_categorias']=dicCategorias

    context = {
        'product_list':product_list,
    }
    return render(request,'index.html',context)

def producto(request, producto_id):
    producto= get_object_or_404(Producto, pk=producto_id)
    return render(request,'producto.html',{'producto':producto})

def categoria(request, categoria_id):
    categoria=get_object_or_404(Categoria,pk=categoria_id)
    product_list = Producto.objects.filter(categoria=categoria)
    category_list = Categoria.objects.all()
    context = {
        'product_list':product_list,
        'category_list':category_list
    }
    return render(request, 'index.html', context)


from tienda.carrito import Cart

def agregarCarrito(request,producto_id):
    producto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(producto,1)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def eliminarProductoCarrito(request,producto_id):
    producto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.remove(producto)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def limpiarCarrito(request):
    CarritoProducto = Cart(request)
    CarritoProducto.clear()
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def carrito(request):
    print(request.session.get("cart"))
    return render(request,'carrito.html')
