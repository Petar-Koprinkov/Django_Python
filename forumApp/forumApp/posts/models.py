from django.db import models

from forumApp.posts.choices import LanguageChoices
from forumApp.posts.validators import BadLanguageValidator


class Books(models.Model):
    title = models.CharField(
        max_length=100,
    )

    content = models.TextField(
        validators=[BadLanguageValidator(words=['fuck'])]
    )

    author = models.CharField(
        max_length=100
    )

    created_at = models.DateField(
        auto_now_add=True
    )

    language = models.CharField(
        max_length=30,
        choices=LanguageChoices.choices,
        default=LanguageChoices.Other
    )
