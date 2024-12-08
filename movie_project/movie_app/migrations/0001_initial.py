# Generated by Django 5.1.3 on 2024-12-06 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=6)),
                ('genre', models.CharField(max_length=30)),
                ('intro', models.TextField(max_length=150)),
                ('poster', models.ImageField(upload_to='posters')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
    ]
