# Generated by Django 4.0.1 on 2022-02-21 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0037_producto_codigo_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalledescargaproducto',
            name='costo_anterior',
        ),
        migrations.RemoveField(
            model_name='detalledescargaproducto',
            name='precio_anterior',
        ),
    ]
