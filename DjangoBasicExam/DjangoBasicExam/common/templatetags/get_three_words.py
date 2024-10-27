from django import template

register = template.Library()


@register.filter
def first_three_words(value):
    words = value.split()[:3]
    return " ".join(words)



