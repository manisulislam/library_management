# Generated by Django 4.2.7 on 2023-12-30 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_rename_comment_bookreviewmodel_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreviewmodel',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.buybookmodel'),
        ),
    ]
