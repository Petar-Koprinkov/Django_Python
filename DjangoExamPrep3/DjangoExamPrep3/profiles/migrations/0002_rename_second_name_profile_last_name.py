# Generated by Django 5.1.2 on 2024-10-26 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='second_name',
            new_name='last_name',
        ),
    ]
