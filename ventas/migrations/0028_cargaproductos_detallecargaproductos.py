# Generated by Django 4.0.1 on 2022-02-18 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0027_alter_detalleventa_precio_alter_detalleventa_total_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CargaProductos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_carga', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.CharField(help_text='Descripcion de la carga de producto', max_length=200)),
                ('sucursal', models.ForeignKey(help_text='Sucursal donde se realiza la carga', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ventas.sucursal')),
                ('usuario', models.ForeignKey(help_text='Ingrese el usuario que realiza la carga', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCargaProductos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(help_text='Ingrese la cantidad del producto', null=True)),
                ('costo', models.FloatField(help_text='Ingrese el costo del producto', null=True)),
                ('precio', models.FloatField(help_text='Ingrese el precio a como se va dar el producto en la venta', null=True)),
                ('total', models.FloatField(null=True)),
                ('carga_producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ventas.cargaproductos')),
                ('presentacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ventas.presentacion')),
                ('producto', models.ForeignKey(help_text='Ingrese el nombre del producto', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ventas.producto')),
            ],
        ),
    ]
