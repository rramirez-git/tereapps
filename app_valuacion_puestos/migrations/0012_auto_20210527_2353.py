# Generated by Django 3.0.7 on 2021-05-27 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_valuacion_puestos', '0011_auto_20210518_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factor',
            name='ponderacion_nivel_1',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='%'),
        ),
    ]