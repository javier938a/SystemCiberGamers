# Generated by Django 4.0.1 on 2022-01-30 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0010_factura_total_con_iva_factura_total_por_iva_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Factura',
            new_name='FacturaVentas',
        ),
    ]
