# Generated by Django 4.2.1 on 2023-07-04 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0003_meetup_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='meetup',
            name='location',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='meetups.location'),
            preserve_default=False,
        ),
    ]
