# Generated by Django 3.2.8 on 2022-04-20 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0024_auto_20220419_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='mantenimiento',
            name='equipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='libreria.equipo'),
        ),
        migrations.AlterField(
            model_name='mantenimiento',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
