# Generated by Django 4.2 on 2023-04-09 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('facebook', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
                ('twitter', models.CharField(max_length=100)),
                ('pinterest', models.CharField(max_length=100)),
                ('linkedin', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
