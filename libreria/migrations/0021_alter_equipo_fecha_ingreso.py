# Generated by Django 3.2.8 on 2022-04-17 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0020_auto_20220417_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='fecha_ingreso',
            field=models.DateTimeField(null=True),
        ),
    ]
