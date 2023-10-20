from django import template

register = template.Library()

@register.filter
def concat(value, arg):
    return str(value) + str(arg)

