from django.urls import path
from . import views

urlpatterns=[
    path('suma/<int:a>/<int:b>',views.suma,name='suma'),
    path('resta/<int:a>/<int:b>',views.resta,name='resta'),
    path('multiplicacion/<int:a>/<int:b>', views.multiplicacion,name='multiplicacion'),
    path('division/<int:a>/<int:b>',views.division,name='division')
]