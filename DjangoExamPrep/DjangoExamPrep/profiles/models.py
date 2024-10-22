from django.core.validators import MinLengthValidator
from django.db import models

from DjangoExamPrep.profiles.validators import IsAlphaNumericValidator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(2), IsAlphaNumericValidator()],
    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )


