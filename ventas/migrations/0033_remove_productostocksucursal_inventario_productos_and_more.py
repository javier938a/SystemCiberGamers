# Generated by Django 4.0.1 on 2022-02-20 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0032_detallecargaproductos_nueva_cantidad_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productostocksucursal',
            name='inventario_productos',
        ),
        migrations.AddField(
            model_name='productostocksucursal',
            name='sucursal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ventas.sucursal'),
        ),
    ]
