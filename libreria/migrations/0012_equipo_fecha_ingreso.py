# Generated by Django 3.2.8 on 2022-04-17 22:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0011_remove_equipo_fecha_ingreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='fecha_ingreso',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de ingreso'),
        ),
    ]
