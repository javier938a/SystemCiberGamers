# Generated by Django 4.0.1 on 2022-02-19 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0030_detallecargaproductos_tipo_prod'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecargaproductos',
            name='cantidad_anterior',
            field=models.FloatField(help_text='Ingrese la cantidad anterior del producto', null=True),
        ),
        migrations.AddField(
            model_name='detallecargaproductos',
            name='costo_anterior',
            field=models.FloatField(help_text='Ingrese el costo anterior', null=True),
        ),
        migrations.AddField(
            model_name='detallecargaproductos',
            name='precio_anterior',
            field=models.FloatField(help_text='Ingrese el precio anterior', null=True),
        ),
    ]
