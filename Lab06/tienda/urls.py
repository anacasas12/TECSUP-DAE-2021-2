from django.urls import path

from . import views

app_name='tienda'
urlpatterns = [
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
    path('',views.index, name='index')
]
