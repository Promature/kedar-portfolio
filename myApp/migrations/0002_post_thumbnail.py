# Generated by Django 4.2.2 on 2023-06-24 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='placeholder.webp', null=True, upload_to='images'),
        ),
    ]
