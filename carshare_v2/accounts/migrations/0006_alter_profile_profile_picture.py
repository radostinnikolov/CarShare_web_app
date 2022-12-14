# Generated by Django 4.1.3 on 2022-12-13 09:25

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_appuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(blank=True, default='images/Default-welcomer.png', max_length=255, null=True),
        ),
    ]
