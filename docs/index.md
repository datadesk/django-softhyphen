django-softhyphen
=================

A Python library for hyphenating HTML in your Django project

Repurposed from Filipe Fortes' [excellent AppEngine app](https://github.com/fortes/softhyphen).

Features
--------

* Use the ``&shy;`` [HTML entity](http://www.w3.org/TR/html4/struct/text.html#h-9.3.3) to hyphenate text. Works well with [text-align:justify;](http://www.w3schools.com/cssref/pr_text_text-align.asp)
* Can be called as a function from inside Python code or as a filter in the Django template
* Supports more than 25 languages

Getting started
---------------

Install it.

```bash
$ pip install django-softhyphen
```

Add it to the INSTALLED_APPS in your settings.py

```python
INSTALLED_APPS = (
    ...
    'softhyphen',
    ...
)
```

Use it in as a function.

```python
>>> from softhyphen.html import hyphenate
>>> hyphenate("<h1>I love hyphenation</h1>")
"<h1>I love hy&shy;phen&shy;a&shy;tion</h1>"
>>> # It is English by default, but you can provide another language.
>>> hyphenate("<h1>Me encanta guiones</h1>", language="es-es")
<h1>Me en&shy;can&shy;ta gu&shy;io&shy;nes</h1>
```

Or use it as a template filter.

```django+html
{% load softhyphen_tags %}
{{ text|softhyphen }}
{# You can specify another language as an argument. English is the default #}
{{ text|softhyphen:"es-es" }}
```

(Warning! Because of its overhead, the filter is not recommended in production if it needs to run each time the page loads.)

Other resources
---------------

[![Build Status](https://travis-ci.org/datadesk/django-softhyphen.png?branch=master)](https://travis-ci.org/datadesk/django-softhyphen)
[![PyPI version](https://badge.fury.io/py/django-softhyphen.png)](http://badge.fury.io/py/django-softhyphen)
[![Coverage Status](https://coveralls.io/repos/datadesk/django-softhyphen/badge.png?branch=master)](https://coveralls.io/r/datadesk/django-softhyphen?branch=master)

* Repo: [https://github.com/datadesk/django-softhyphen](https://github.com/datadesk/django-softhyphen)
* Issues: [https://github.com/datadesk/django-softhyphen/issues](https://github.com/datadesk/django-softhyphen/issues)
* Packaging: [https://pypi.python.org/pypi/django-softhyphen](https://pypi.python.org/pypi/django-softhyphen)
* Testing: [https://travis-ci.org/datadesk/django-softhyphen](https://travis-ci.org/datadesk/django-softhyphen)
* Coverage: [https://coveralls.io/r/datadesk/django-softhyphen](https://coveralls.io/r/datadesk/django-softhyphen)

