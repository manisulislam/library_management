# Generated by Django 4.2.7 on 2023-12-29 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_useraccount_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='initial_deposit_date',
        ),
    ]
