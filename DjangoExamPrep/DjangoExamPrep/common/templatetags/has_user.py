from django import template
from DjangoExamPrep.utils import get_profile_object


register = template.Library()


@register.simple_tag()
def has_user():
    return get_profile_object()
