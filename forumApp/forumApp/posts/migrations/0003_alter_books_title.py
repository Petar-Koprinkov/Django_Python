# Generated by Django 5.1.1 on 2024-10-05 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_books_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]