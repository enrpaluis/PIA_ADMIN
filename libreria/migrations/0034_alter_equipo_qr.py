# Generated by Django 3.2.8 on 2022-04-20 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0033_auto_20220420_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='qr',
            field=models.CharField(max_length=100, verbose_name='QR'),
        ),
    ]
