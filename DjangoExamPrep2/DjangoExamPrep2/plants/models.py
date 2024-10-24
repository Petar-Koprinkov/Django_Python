from django.core.validators import MinLengthValidator
from django.db import models

from DjangoExamPrep2.plants.choices import PlantChoices
from DjangoExamPrep2.plants.validators import AlphaValidator


class Plant(models.Model):

    plant_type = models.CharField(
        max_length=14,
        choices= PlantChoices.choices,
    )

    name = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2), AlphaValidator()],
    )

    image_url = models.URLField()

    description = models.TextField()

    price = models.FloatField()
