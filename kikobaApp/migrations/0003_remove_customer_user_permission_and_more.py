# Generated by Django 5.0.2 on 2024-04-01 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kikobaApp', '0002_customer_user_permission_customer_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='User_permission',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='group',
        ),
    ]