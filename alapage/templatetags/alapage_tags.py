# -*- coding: utf-8 -*-

from django import template
from alapage.conf import EDIT_MODE


register = template.Library()

@register.simple_tag
def get_edit_mode():
    return EDIT_MODE