from html import hyphenate_html
from django.test import TestCase


class SoftHyphenTest(TestCase):
    
    def test_method(self):
        """
        Test usage of the hyphenation method directly.
        """
        before = "<h1>I love hyphenation</h1>"
        after = hyphenate_html(before)
        self.failUnlessEqual(after, "<h1>I love hy&shy;phen&shy;a&shy;tion</h1>")





