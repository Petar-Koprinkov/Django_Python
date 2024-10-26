# Generated by Django 5.1.2 on 2024-10-26 15:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1.0)]),
            preserve_default=False,
        ),
    ]
