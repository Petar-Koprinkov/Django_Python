from django.core.validators import MinLengthValidator
from django.db import models

from DjangoBasicExam.authors.validators import AlphaValidator, ExactlyNumbersValidator


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[MinLengthValidator(4), AlphaValidator()],
    )

    last_name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2), AlphaValidator()],
    )

    passcode = models.CharField(
        validators=[ExactlyNumbersValidator(6)],
        help_text='Your passcode must be a combination of 6 digits'
    )

    pets_number = models.PositiveSmallIntegerField()

    info = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )
