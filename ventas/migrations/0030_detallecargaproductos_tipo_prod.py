# Generated by Django 4.0.1 on 2022-02-19 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0029_cargaproductos_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecargaproductos',
            name='tipo_prod',
            field=models.CharField(help_text='Ingrese el tipo de producto', max_length=100, null=True),
        ),
    ]
