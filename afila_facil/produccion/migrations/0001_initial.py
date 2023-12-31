# Generated by Django 4.2.1 on 2023-07-18 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materias_primas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto_completo', models.BooleanField(default=False)),
                ('productos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produccion', to='materias_primas.productos')),
            ],
            options={
                'verbose_name': 'Produccion',
                'db_table': 'produccion',
            },
        ),
    ]
