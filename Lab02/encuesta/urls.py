from . import views
from django.urls import path

app_name ='encuesta'

urlpatterns = [
    path('',views.index,name='index'),
    path('enviar', views.enviar, name='enviar'),
]