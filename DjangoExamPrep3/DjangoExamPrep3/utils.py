from django.db.models import Sum

from DjangoExamPrep3.cars.models import Car
from DjangoExamPrep3.profiles.models import Profile


def get_profile():
    return Profile.objects.first()


def get_total_price():
    return Car.objects.all().aggregate(total=Sum('price'))['total']
