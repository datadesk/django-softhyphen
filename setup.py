#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from distutils.core import Command


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from django.conf import settings
        settings.configure(
            DATABASES={
                'default': {
                    'NAME': ':memory:',
                    'ENGINE': 'django.db.backends.sqlite3'
                }
            },
            INSTALLED_APPS=('softhyphen',)
        )
        from django.core.management import call_command
        import django
        if django.VERSION[:2] >= (1, 7):
            django.setup()
        call_command('test', 'softhyphen')


setup(
    name='django-softhyphen',
    version='1.1.0',
    packages=[
        'softhyphen',
        'softhyphen.dicts',
        'softhyphen.templatetags',
    ],
    include_package_data=True,
    description='A Python library for hyphenating HTML in your Django project',
    url='https://github.com/datadesk/django-softhyphen/',
    author='Ben Welsh',
    author_email='ben.welsh@gmail.com',
    install_requires=(
        'beautifulsoup4',
        'six'
    ),
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ),
    cmdclass={'test': TestCommand}
)
