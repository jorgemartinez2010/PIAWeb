# Generated by Django 3.2.2 on 2021-05-17 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=60)),
                ('nombre', models.CharField(max_length=60)),
                ('modelo', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Estante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=60)),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Locker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=60)),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Mueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=60)),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=60)),
            ],
        ),
    ]
