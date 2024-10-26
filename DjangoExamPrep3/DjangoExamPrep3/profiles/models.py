from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from DjangoExamPrep3.profiles.validators import CustomMinLengthValidator, IsAlphaNumericValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[CustomMinLengthValidator(3), IsAlphaNumericValidator()]
    )

    email = models.EmailField()

    age = models.IntegerField(
        validators=[MinValueValidator(21)],
        help_text="Age requirement: 21 years and above."
    )

    password = models.CharField(
        max_length=20,
    )

    first_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )




