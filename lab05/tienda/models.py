from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=200)
    precio=models.DecimalField(max_digits=6, decimal_places=2)
    stock=models.IntegerField(default=0)
    pub_date=models.DateTimeField('date publised')

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombres=models.CharField(max_length=300)
    apellidos=models.CharField(max_length=200)
    dni=models.CharField(max_length=8)
    telefono=models.CharField(max_length=9)
    direccion=models.CharField(max_length=200)
    email=models.EmailField(blank=True)
    fecha_nacimiento=models.DateField(null=False)
    fecha_publicacion=models.DateField(null=False)

    def __str__(self):
        return self.nombres