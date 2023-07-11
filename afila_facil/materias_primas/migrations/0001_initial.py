# Generated by Django 4.2.1 on 2023-07-11 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Producto',
                'db_table': 'productos',
            },
        ),
    ]
