from django import template

register = template.Library()

@register.filter('cut')
def cut(value, arg):
    """
    cuts all values of arg from string
    """
    return value.replace(arg, '')

### Use in place of decorator
#register.filter('cut',cut)
