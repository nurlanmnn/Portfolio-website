# Generated by Django 4.2 on 2023-04-09 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_text_aboutme_p1_aboutme_p2_aboutme_p3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('p1', models.TextField()),
                ('p2', models.TextField()),
                ('p3', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
    ]
