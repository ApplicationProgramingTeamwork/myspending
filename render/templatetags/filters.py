import base64
from django import template

register = template.Library()


@register.filter
def contains_any_ic(string, words):
    """Check if any of the words in a comma-separated list are in the string."""
    string_lower = string.lower()
    return any(word.lower() in string_lower for word in words.split(','))


@register.filter
def b64encode(value):
    """Encode a string to base64."""
    return base64.b64encode(value).decode('utf-8')
