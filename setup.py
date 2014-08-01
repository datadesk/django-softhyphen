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
        call_command('test', 'softhyphen')


setup(
    name='django-softhyphen',
    version='1.0.1',
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
        'beautifulsoup4>=4.3.2',
        'six>=1.5.1'
    ),
    cmdclass={'test': TestCommand}
)
