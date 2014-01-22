#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import six
from .html import hyphenate
from django.test import TestCase
from .templatetags.softhyphen_tags import softhyphen


class SoftHyphenTest(TestCase):

    def test_simple_call(self):
        """
        Test simple usage of the hyphenation method directly.
        """
        before = "<h1>I love hyphenation</h1>"
        after = hyphenate(before)
        self.failUnlessEqual(
            after,
            "<h1>I love hy&shy;phen&shy;a&shy;tion</h1>"
        )

    def test_tag_blacklist_call(self):
        """
        Test the blacklist to make sure some tags don't get hyphenated.
        """
        before = "<code>I love hyphenation</code>"
        after = hyphenate(before)
        self.failUnlessEqual(after, "<code>I love hyphenation</code>")

    def test_spanish_call(self):
        """
        Test usage of the blacklist with spanish
        """
        before = "<h1>Me encanta guiones</h1>"
        after = hyphenate(before, language='es-es')
        self.failUnlessEqual(
            after,
            "<h1>Me en&shy;can&shy;ta gu&shy;io&shy;nes</h1>"
        )

    def test_braille_language_call(self):
        """
        Test usage with Braille language call.
        """
        before = "<h1>⠓⠁⠍-⠃⠥⠗⠛⠑⠗</h1>"
        hyphenate(before, language='hu-hu')

    def test_foo_language_call(self):
        """
        Test usage with a made up language.
        """
        before = "<h1>I love hyphenation</h1>"
        after = hyphenate(before, language='foobar')
        self.failUnlessEqual(
            after,
            "<h1>I love hy&shy;phen&shy;a&shy;tion</h1>"
        )

    def test_simple_filter(self):
        """
        Test simple usage of the hyphenation method via the templatetag.
        """
        before = "<h1>I love hyphenation</h1>"
        after = softhyphen(before)
        self.failUnlessEqual(
            after,
            "<h1>I love hy&shy;phen&shy;a&shy;tion</h1>"
        )

    def test_spanish_filter(self):
        """
        Test usage of the blacklist with spanish via the templatetag.
        """
        before = "<h1>Me encanta guiones</h1>"
        after = softhyphen(before, language='es-es')
        self.failUnlessEqual(
            after,
            six.u("<h1>Me en&shy;can&shy;ta gu&shy;io&shy;nes</h1>")
        )

    def test_russian_filter(self):
        """
        Test usage of the templatetag with Russian.

        Also tests that the tag works properly with non-ascii characters.
        """
        before = six.u('<h1>\u043f\u0435\u0440\u0435.</h1>')
        after = softhyphen(before, language='ru-ru')
        self.failUnlessEqual(
            after,
            six.u('<h1>\u043f\u0435&shy;\u0440\u0435.</h1>')
        )
