# Generated by Django 4.1.3 on 2022-11-22 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friendrequest',
            old_name='receiver_id',
            new_name='receiver',
        ),
        migrations.RenameField(
            model_name='friendrequest',
            old_name='requester_id',
            new_name='requester',
        ),
    ]