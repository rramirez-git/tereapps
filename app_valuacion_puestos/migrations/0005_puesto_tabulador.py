# Generated by Django 3.0.7 on 2021-04-21 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_valuacion_puestos', '0004_auto_20210421_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='puesto',
            name='tabulador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='app_valuacion_puestos.Tabulador'),
            preserve_default=False,
        ),
    ]