from django import template

from DjangoBasicExam.utils import get_profile

register = template.Library()


@register.simple_tag()
def get_profile_tag():
    return get_profile()
