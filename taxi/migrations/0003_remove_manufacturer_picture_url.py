# Generated by Django 4.0.2 on 2022-10-02 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_car_picture_url_driver_picture_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manufacturer',
            name='picture_url',
        ),
    ]
