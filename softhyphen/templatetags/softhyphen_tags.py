# -*- coding: utf-8 -*-
from django import template
register = template.Library()
from softhyphen.html import hyphenate


@register.filter
def softhyphen(value, language="en-us"):
    """
    Hyphenates html.
    """
    return hyphenate(value, language=language)

softhyphen.is_safe = True
