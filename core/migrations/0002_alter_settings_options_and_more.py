# Generated by Django 4.2 on 2023-04-09 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name_plural': 'Settings'},
        ),
        migrations.RenameField(
            model_name='settings',
            old_name='pinterest',
            new_name='github',
        ),
    ]
