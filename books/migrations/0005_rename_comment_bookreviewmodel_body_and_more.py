# Generated by Django 4.2.7 on 2023-12-30 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_remove_bookreviewmodel_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookreviewmodel',
            old_name='comment',
            new_name='body',
        ),
        migrations.RemoveField(
            model_name='bookreviewmodel',
            name='user',
        ),
        migrations.AddField(
            model_name='bookreviewmodel',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]