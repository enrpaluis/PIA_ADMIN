# Generated by Django 3.2.8 on 2022-04-17 21:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0006_alter_equipo_fecha_ingreso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='fecha_ingreso',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
