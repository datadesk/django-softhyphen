from html import hyphenate_html
from django.test import TestCase


class SoftHyphenTest(TestCase):
    
    def test_simple_call(self):
        """
        Test simple usage of the hyphenation method directly.
        """
        before = "<h1>I love hyphenation</h1>"
        after = hyphenate_html(before)
        self.failUnlessEqual(after, "<h1>I love hy&shy;phen&shy;a&shy;tion</h1>")
    
    def test_tag_blacklist(self):
        """
        Test the blacklist to make sure some tags don't get hyphenated.
        """
        before = "<code>I love hyphenation</code>"
        after = hyphenate_html(before)
        self.failUnlessEqual(after, "<code>I love hyphenation</code>")


