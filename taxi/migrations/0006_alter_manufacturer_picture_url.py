# Generated by Django 4.0.2 on 2022-10-18 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0005_alter_manufacturer_picture_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='picture_url',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/'),
        ),
    ]