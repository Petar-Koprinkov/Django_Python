from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models

from DjangoExamPrep2.profiles.validators import CapitalLetterValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(2)],

    )

    first_name = models.CharField(
        max_length=20,
        validators=[CapitalLetterValidator()]
    )

    last_name = models.CharField(
        max_length=20,
        validators=[CapitalLetterValidator()]
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


