# -*- coding: utf-8 -*-
from django import template
register = template.Library()
from softhyphen.html import hyphenate
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter


def softhyphen(value, language="en-us"):
    """
    Hyphenates html.
    """
    return mark_safe(hyphenate(value, language=language))
softhyphen.is_safe = True
softhyphen = stringfilter(softhyphen)
softhyphen = register.filter(softhyphen)


