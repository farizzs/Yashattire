# Generated by Django 3.2.10 on 2023-06-09 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0009_productdb_trending'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdb',
            name='New_Arival',
            field=models.BooleanField(default=False),
        ),
    ]