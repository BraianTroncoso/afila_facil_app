# Generated by Django 4.2.1 on 2023-07-17 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materias_primas', '0005_alter_productos_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.CharField(max_length=100),
        ),
    ]