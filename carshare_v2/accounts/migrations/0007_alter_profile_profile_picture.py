# Generated by Django 4.1.3 on 2022-12-13 09:46

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(blank=True, default='image/upload/v1670924768/pokmkgecsop9suxl9xri.png', max_length=255, null=True),
        ),
    ]
