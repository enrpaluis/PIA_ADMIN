# Generated by Django 3.2.8 on 2022-04-17 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0016_alter_equipo_frecuencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='frecuencia',
        ),
    ]
