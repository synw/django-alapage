from django import template
from alapage.conf import CODE_MODE


register = template.Library()


@register.simple_tag
def iscode_mode():
    return CODE_MODE
