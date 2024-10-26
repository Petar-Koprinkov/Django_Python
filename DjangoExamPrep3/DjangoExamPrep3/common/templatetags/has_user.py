from django import template
from DjangoExamPrep3.utils import get_profile

register = template.Library()


@register.simple_tag()
def has_user():
    return get_profile()