# Generated by Django 4.2.1 on 2023-06-25 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0002_rename_descriontion_meetup_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='image',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]
