# -*- coding: utf-8 -*-
from django import template
from softhyphen.html import hyphenate
register = template.Library()


@register.filter
def softhyphen(value, language=None):
    """
    Hyphenates html.
    """
    return hyphenate(value, language=language)

softhyphen.is_safe = True
