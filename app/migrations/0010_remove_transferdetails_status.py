# Generated by Django 5.1.4 on 2025-03-21 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_transferdetails_options_transferdetails_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transferdetails',
            name='status',
        ),
    ]
