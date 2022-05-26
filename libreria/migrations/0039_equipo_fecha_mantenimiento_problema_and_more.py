# Generated by Django 4.0.3 on 2022-04-20 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0038_mantenimiento_hora'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='mantenimiento',
            name='problema',
            field=models.CharField(choices=[('Pieza Faltante', 'Pieza Faltante'), ('Daño por Accidente', 'Daño por Accidente'), ('Daño por Incendio', 'Daño por Incendio'), ('No enciende', 'No enciende'), ('Otro', 'Otro'), ('No encontrado', 'No encontrado')], max_length=100, null=True, verbose_name='Problema'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='dominio',
            field=models.CharField(choices=[('Propio', 'Propio'), ('Comodato', 'Comodato'), ('Otro', 'Otro')], max_length=100, null=True, verbose_name='Dominio'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='frecuencia',
            field=models.CharField(choices=[('Diario', 'Diario'), ('Semanal', 'Semanal'), ('Mensual', 'Mensual'), ('Semestral', 'Semestral'), ('Anual', 'Anual')], max_length=100, null=True, verbose_name='Frecuencia'),
        ),
    ]
