# templatetags/my_filters.py
from django import template

register = template.Library()


@register.filter
def contains_any_ic(string, words):
    string_lower = string.lower()
    return any(word.lower() in string_lower for word in words.split(','))
