# Generated by Django 4.2 on 2023-05-08 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_alter_productdb_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdb',
            name='Price',
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
    ]