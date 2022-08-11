# Generated by Django 4.0.1 on 2022-02-06 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0016_remove_productostocksucursal_sucursal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventarioproductos',
            name='total',
            field=models.DecimalField(decimal_places=2, help_text='Ingrese el total de el inventario', max_digits=10, null=True),
        ),
    ]