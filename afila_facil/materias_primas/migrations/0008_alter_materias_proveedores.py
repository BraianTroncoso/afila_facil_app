# Generated by Django 4.2.1 on 2023-08-01 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0005_remove_proveedores_produccion'),
        ('materias_primas', '0007_alter_materias_proveedores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materias',
            name='proveedores',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proveedores.proveedores'),
        ),
    ]
