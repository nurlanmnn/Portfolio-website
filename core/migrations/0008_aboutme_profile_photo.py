# Generated by Django 4.2 on 2023-04-10 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_settings_contact_text_settings_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='profile_photo',
            field=models.ImageField(default=' ', upload_to='media/AboutMe/profile_photo'),
            preserve_default=False,
        ),
    ]