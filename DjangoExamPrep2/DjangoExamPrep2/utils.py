from DjangoExamPrep2.profiles.models import Profile


def get_profile():
    return Profile.objects.first()