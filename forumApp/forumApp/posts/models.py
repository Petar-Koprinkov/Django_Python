from django.db import models

from forumApp.posts.choices import LanguageChoices


class Books(models.Model):
    title = models.CharField(
        max_length=100,
    )

    content = models.TextField()

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
