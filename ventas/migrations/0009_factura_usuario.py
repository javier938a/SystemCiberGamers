# Generated by Django 4.0.1 on 2022-01-30 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0008_factura_ventas_factura'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]