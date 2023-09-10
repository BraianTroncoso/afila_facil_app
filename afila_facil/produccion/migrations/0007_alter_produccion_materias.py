# Generated by Django 4.2.1 on 2023-09-04 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materias_primas', '0011_alter_materias_proveedores'),
        ('produccion', '0006_produccion_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produccion',
            name='materias',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='produccion', to='materias_primas.materias'),
        ),
    ]
