# Generated by Django 4.2.1 on 2023-07-19 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0003_produccion_produccion_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='produccion',
            name='produccion_total',
            field=models.IntegerField(default=0),
        ),
    ]
