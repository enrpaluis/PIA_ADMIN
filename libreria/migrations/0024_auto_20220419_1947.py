# Generated by Django 3.2.8 on 2022-04-20 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0023_mantenimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mantenimiento',
            name='equipo',
        ),
        migrations.RemoveField(
            model_name='mantenimiento',
            name='fecha',
        ),
        migrations.AlterField(
            model_name='mantenimiento',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
