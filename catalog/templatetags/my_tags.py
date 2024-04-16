from django import template

register = template.Library()


@register.filter
def media_path(filename):
    if filename:
        return f'/media/{filename}'
    return '#'
