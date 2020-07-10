# Generated by Django 3.0.8 on 2020-07-10 12:19

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0003_dev_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='post',
        ),
        migrations.AddField(
            model_name='site',
            name='image',
            field=cloudinary.models.CloudinaryField(default='screenshot', max_length=255),
        ),
        migrations.AddField(
            model_name='site',
            name='url',
            field=models.URLField(default='websiteurl'),
        ),
    ]