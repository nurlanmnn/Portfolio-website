# Generated by Django 4.2 on 2023-04-10 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_projectcategory_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_link',
            field=models.CharField(default=' ', max_length=250),
            preserve_default=False,
        ),
    ]