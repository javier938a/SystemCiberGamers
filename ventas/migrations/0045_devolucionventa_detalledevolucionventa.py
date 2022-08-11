# Generated by Django 4.0.1 on 2022-06-05 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0044_alter_venta_total_con_iva'),
    ]

    operations = [
        migrations.CreateModel(
            name='DevolucionVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(help_text='ingrese la descripcion de la devolucion')),
                ('fecha_devolucion', models.DateField(blank=True, help_text='Ingrese la fecha de devolucion', null=True)),
                ('factura', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ventas.venta')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleDevolucionVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_devolver', models.IntegerField(help_text='Ingrese la cantidad a devolver')),
                ('precio', models.FloatField(blank=True, help_text='Ingrese el precio del producto', null=True)),
                ('total', models.FloatField(blank=True, help_text='Ingrese el total de la devolucion', null=True)),
                ('devolucion_venta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ventas.devolucionventa')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ventas.producto')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
