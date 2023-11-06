# Generated by Django 4.2.6 on 2023-10-26 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('autor', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('anio', models.IntegerField())
            ],
        ),
           migrations.CreateModel(
            name='Maquillaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30))
            ],
        ),
    ]
