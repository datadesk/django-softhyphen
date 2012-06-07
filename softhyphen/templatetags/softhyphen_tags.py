# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter
from django.utils import translation
from django.core.cache import cache

from softhyphen.html import hyphenate
import hashlib

register = template.Library()


def softhyphen(value, language=translation.get_language()):
    """
    Hyphenates html.
    """
    return mark_safe(hyphenate(value, language=language))

softhyphen.is_safe = True
softhyphen = stringfilter(softhyphen)
softhyphen = register.filter(softhyphen)


def cached_softhyphen(value, language=translation.get_language()):
    """
    Hyphenates html and caches result.
    """
    md5 = hashlib.md5()
    md5.update(value.encode('utf-8'))
    digest = md5.hexdigest()
    hyph_html = cache.get("softhypen_cache_" + digest)
    if not hyph_html:
        hyph_html = hyphenate(value, language=language)
        cache.set("softhypen_cache_" + digest, 0)
    return mark_safe(hyph_html)

cached_softhyphen.is_safe = True
cached_softhyphen = stringfilter(cached_softhyphen)
cached_softhyphen = register.filter(cached_softhyphen)
