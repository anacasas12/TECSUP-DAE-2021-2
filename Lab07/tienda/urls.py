from django.urls import path

from . import views

app_name='tienda'
urlpatterns = [
    path('agregarCarrito/<int:producto_id>',views.agregarCarrito,name='agregarCarrito'),
    path('carrito',views.carrito,name='carrito'),
    path('eliminarProductoCarrito/<int:producto_id>',views.eliminarProductoCarrito,name="eliminarProductoCarrito"),
    path('limpiarCarrito',views.limpiarCarrito,name='limpiarCarrito'),
    path('producto/<int:producto_id>/', views.producto, name='producto'),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
    path('',views.index, name='index')
]
