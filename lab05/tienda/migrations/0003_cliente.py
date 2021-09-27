# Generated by Django 3.2.6 on 2021-09-27 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=300)),
                ('apellidos', models.CharField(max_length=200)),
                ('dni', models.CharField(max_length=8)),
                ('telefono', models.CharField(max_length=9)),
                ('direccion', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_publicacion', models.DateField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.categoria')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.producto')),
            ],
        ),
    ]
