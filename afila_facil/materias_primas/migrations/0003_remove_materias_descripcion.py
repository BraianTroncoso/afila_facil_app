# Generated by Django 4.2.1 on 2023-08-01 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materias_primas', '0002_rename_productos_materias_alter_materias_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materias',
            name='descripcion',
        ),
    ]
