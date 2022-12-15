# Generated by Django 4.1.3 on 2022-12-12 16:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_appuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='email',
            field=models.CharField(max_length=50, unique=True, validators=[django.core.validators.EmailValidator]),
        ),
    ]