from . import views
from django.urls import path

app_name ='radiocilindro'

urlpatterns = [
    path('', views.index, name='index'),
    path('respuesta/', views.respuesta, name='respuesta')
]
