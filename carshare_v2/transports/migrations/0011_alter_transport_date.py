# Generated by Django 4.1.3 on 2022-12-12 15:42

import carshare_v2.transports.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transports', '0010_alter_transport_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='date',
            field=models.DateField(validators=[carshare_v2.transports.models.validate_date_is_not_in_the_past]),
        ),
    ]
