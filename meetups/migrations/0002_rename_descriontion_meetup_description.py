# Generated by Django 4.2.1 on 2023-06-23 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetup',
            old_name='descriontion',
            new_name='description',
        ),
    ]
