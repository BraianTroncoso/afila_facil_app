# Generated by Django 4.2.1 on 2023-07-19 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materias_primas', '0001_initial'),
        ('produccion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccion',
            name='productos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='produccion', to='materias_primas.productos'),
        ),
    ]
