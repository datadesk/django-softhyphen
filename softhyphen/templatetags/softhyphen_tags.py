# -*- coding: utf-8 -*-
from django import template
register = template.Library()
from softhyphen.html import hyphenate
from django.utils.safestring import mark_safe


@register.filter(is_safe=True)
def softhyphen(value, language="en-us"):
    """
    Hyphenates html.
    """
    return mark_safe(hyphenate(value, language=language))
