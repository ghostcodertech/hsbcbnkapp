# Generated by Django 5.1.4 on 2025-04-16 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_account_bank_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='back_id_image',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='front_id_image',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='proof_of_employment',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='proof_of_income',
        ),
    ]
