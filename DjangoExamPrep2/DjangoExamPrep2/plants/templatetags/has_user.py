from django import template
from DjangoExamPrep2.utils import get_profile

register = template.Library()


@register.simple_tag()
def has_user():
    return get_profile()