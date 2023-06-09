# Generated by Django 3.2.10 on 2023-06-12 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FrontendApp', '0008_auto_20230612_2056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkout',
            old_name='quantity',
            new_name='Quantity',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='User_Name',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Placed', 'Placed'), ('Cancelled', 'Cancelled'), ('Delivered', 'Delivered')], default='Pending', max_length=20)),
                ('invoice_id', models.CharField(max_length=100)),
                ('order_id', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='checkout',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_checkouts', to='FrontendApp.order'),
        ),
    ]
