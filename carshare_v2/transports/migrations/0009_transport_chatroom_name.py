# Generated by Django 4.1.3 on 2022-12-08 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transports', '0008_alter_transport_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='transport',
            name='chatroom_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]