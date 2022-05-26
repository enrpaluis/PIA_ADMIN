# Generated by Django 3.2.8 on 2022-04-17 22:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0012_equipo_fecha_ingreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='fecha_hora',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='equipo',
            name='ficha_mantenimiento',
            field=models.URLField(null=True, verbose_name='Ficha de Mantenimiento'),
        ),
    ]