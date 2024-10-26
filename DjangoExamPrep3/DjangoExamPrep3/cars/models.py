from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from DjangoExamPrep3.cars.choices import TypeChoices
from DjangoExamPrep3.cars.validators import YearValidator
from DjangoExamPrep3.profiles.models import Profile


class Car(models.Model):
    type = models.CharField(
        max_length=10,
        choices=TypeChoices.choices
    )

    model = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(1)]
    )

    year = models.IntegerField(
        validators=[YearValidator(1999, 2030)]
    )

    image_url = models.URLField(
        unique=True,
        error_messages={
            'unique': 'This image URL is already in use! Provide a new one."'
        }
    )

    price = models.FloatField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1.0)]
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='cars',
    )




