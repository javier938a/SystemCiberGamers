# Generated by Django 4.0.1 on 2022-02-17 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0026_alter_inventarioproductos_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleventa',
            name='precio',
            field=models.FloatField(help_text='Ingrese el precio del producto', null=True),
        ),
        migrations.AlterField(
            model_name='detalleventa',
            name='total',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='total_con_iva',
            field=models.FloatField(help_text='Total de la suma de todos los productos mas el total del iva', null=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='total_iva',
            field=models.FloatField(help_text='Total resultante de multiplicar el total por el procentaje de iva', null=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='total_sin_iva',
            field=models.FloatField(help_text='Total de la suma de todos los productos sin iva', null=True),
        ),
    ]
