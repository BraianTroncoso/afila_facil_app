# Generated by Django 4.2.1 on 2023-07-11 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materias_primas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='img',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]