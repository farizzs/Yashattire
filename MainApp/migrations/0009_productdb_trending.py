# Generated by Django 3.2.10 on 2023-06-01 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0008_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdb',
            name='Trending',
            field=models.BooleanField(default=False),
        ),
    ]
