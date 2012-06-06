# -*- coding: utf-8 -*-
from django import template
register = template.Library()
from softhyphen.html import hyphenate
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter
#from django.conf import Settings  #TODO: get default language from settings
from django.core.cache import cache
import hashlib
from time import time


def softhyphen(value, language='en-US'):
    """
    Hyphenates html.
    """
    return mark_safe(hyphenate(value, language=language))

softhyphen.is_safe = True
softhyphen = stringfilter(softhyphen)
softhyphen = register.filter(softhyphen)


def cached_softhyphen(value, language='de-DE'):
    """
    Hyphenates html and caches result.
    """
    start = time()
    md5 = hashlib.md5()
    md5.update(value.encode('utf-8'))
    digest = md5.hexdigest()
    hyph_html = cache.get("softhypen_cache_" + digest)
    end = time()
    print "hit: ", end - start
    if not hyph_html:
        start = time()
        hyph_html = hyphenate(value, language=language)
        cache.set("softhypen_cache_" + digest, 0)
        end = time()
        print "no hit: ", end - start
    return mark_safe(hyph_html)

cached_softhyphen.is_safe = True
cached_softhyphen = stringfilter(cached_softhyphen)
cached_softhyphen = register.filter(cached_softhyphen)
