# Generated by Django 4.2.1 on 2023-07-29 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0005_rename_productos_produccion_materias'),
        ('materias_primas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Productos',
            new_name='Materias',
        ),
        migrations.AlterModelOptions(
            name='materias',
            options={'verbose_name': 'Materia'},
        ),
        migrations.AlterModelTable(
            name='materias',
            table='materias',
        ),
    ]
