# Generated by Django 3.2.8 on 2022-04-20 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0026_alter_mantenimiento_equipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mantenimiento',
            name='equipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='libreria.equipo'),
        ),
    ]
