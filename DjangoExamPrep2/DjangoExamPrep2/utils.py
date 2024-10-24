from DjangoExamPrep2.plants.models import Plant
from DjangoExamPrep2.profiles.models import Profile


def get_profile():
    return Profile.objects.first()


def get_stars():
    return Plant.objects.all()
