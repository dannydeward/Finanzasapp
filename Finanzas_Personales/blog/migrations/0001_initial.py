# Generated by Django 4.0.1 on 2022-05-13 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('Contenido', models.CharField(max_length=500)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('created', models.DateTimeField(auto_now=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('categorias', models.ManyToManyField(to='blog.categoria')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
        ),
    ]