# Generated by Django 3.2.8 on 2022-04-17 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0005_rename_clave_equipo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='fecha_ingreso',
            field=models.DateField(null=True, verbose_name='Fecha de Ingreso'),
        ),
    ]