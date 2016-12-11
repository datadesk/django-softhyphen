"""
Hyphenates an HTML fragement using soft hyphens

Author by Filipe Fortes, modified by Ben Welsh
"""
from __future__ import absolute_import

import os
import re
import six
from bs4 import BeautifulSoup
from django.utils.translation import get_language
from .hyphenator import Hyphenator
from bs4.element import PreformattedString


class DontEscapeDammit(PreformattedString):
    """
    A BeautifulSoup trick that lets us insert a `&shy;` into the HTML
    without BS escaping the `&` and turning it into `&amp;shy;`.
    """
    def output_ready(self, formatter=None):
        self.format_string(self, formatter)
        return self.PREFIX + self + self.SUFFIX


def hyphenate(html, language=None, hyphenator=None, blacklist_tags=(
    'code', 'tt', 'pre', 'head', 'title', 'script', 'style', 'meta', 'object',
    'embed', 'samp', 'var', 'math', 'select', 'option', 'input', 'textarea',
    'span')
        ):
    """
    Hyphenate a fragement of HTML

    >>> hyphenate('<p>It is <em>beautiful</em> outside today!</p>')
    u'<p>It is <em>beau&shy;ti&shy;ful</em> out&shy;side today!</p>'

    >>> hyphenate('O paralelepipedo atrevessou', 'pt-br')
    u'O pa&shy;ra&shy;le&shy;le&shy;pi&shy;pe&shy;do atre&shy;ves&shy;sou'

    Content inside <code>, <tt>, and <pre> blocks is not hyphenated
    >>> hyphenate('Document: <code>document + page_status</code>')
    u'Doc&shy;u&shy;ment: <code>document + page_status</code>'

    Short words are not hyphenated

    >>> hyphenate("<p>The brave men, living and dead.</p>")
    u'<p>The brave men, liv&shy;ing and dead.</p>'
    """
    # Load hyphenator if one is not provided
    if not language:
        language = get_language() or 'en-us'

    if language == 'en':
        language = 'en-us'
    elif '-' not in language:
        # Language code is "en-us", "it-it", "nl-nl"
        language = "{0}-{0}".format(language)

    if not hyphenator:
        hyphenator = get_hyphenator_for_language(language)

    # Create HTML tree
    soup = BeautifulSoup(html, "html.parser")

    # Recursively hyphenate each element
    hyphenate_element(soup, hyphenator, blacklist_tags)

    return fix_linebreaks(six.text_type(soup))


# Constants
SOFT_HYPHEN = r'&shy;'
SPACE = r' '
STRIP_WHITESPACE = re.compile('\w+', re.MULTILINE | re.UNICODE)


def blacklist(name, blacklist):
    return name in blacklist


def hyphenate_element(soup, hyphenator, blacklist_tags):
    """
    Hyphenate the text within an element, returning the hyphenated version
    Walks the DOM Tree to track down all text
    """
    # Find any element with text in it
    paragraphs = soup.findAll(text=lambda text: len(text) > 0)
    for paragraph in paragraphs:
        # Make sure element isn't on blacklist
        if not blacklist(paragraph.parent.name, blacklist_tags):
            # Replace text with hyphened version
            new_string = STRIP_WHITESPACE.sub(
                (lambda x: hyphenator.inserted(x.group(), SOFT_HYPHEN)),
                paragraph
            )
            paragraph.replaceWith(DontEscapeDammit(new_string))
    return soup


DICTIONARIES = {
    'cs-cz': 'hyph_cs_CZ',
    'da-dk': 'hyph_da_DK',
    'de-ch': 'hyph_de_CH',
    'de-de': 'hyph_de_DE',
    'el-gr': 'hyph_el_GR',
    'en-ca': 'hyph_en_CA',
    'en-gb': 'hyph_en_GB',
    'en-us': 'hyph_en_US',
    'es-es': 'hyph_es_ES',
    'fi-fi': 'hyph_fi_FI',
    'ga-ie': 'hyph_ga_IE',
    'hu-hu': 'hyph_hu_HU',
    'ia': 'hyph_ia',
    'id-id': 'hyph_id_ID',
    'is-is': 'hyph_is_IS',
    'it-it': 'hyph_it_IT',
    'lt-lt': 'hyph_lt_LT',
    'nl-nl': 'hyph_nl_NL',
    'pl-pl': 'hyph_pl_PL',
    'pt-br': 'hyph_pt_BR',
    'pt-pt': 'hyph_pt_PT',
    'ro-ro': 'hyph_ro_RO',
    'ru-ru': 'hyph_ru_RU',
    'sh': 'hyph_sh',
    'sk-sk': 'hyph_sk_SK',
    'sl-si': 'hyph_sl_SI',
    'sr': 'hyph_sr',
    'sv-se': 'hyph_sv_SE',
    'uk-ua': 'hyph_uk_UA'
}


def get_hyphenator_for_language(language):
    """
    Create a Hyphenator for the given language. Uses English if the
    language is not found.

    >>> get_hyphenator_for_language('ru-ru') #doctest: +ELLIPSIS
    <hyphenator.Hyphenator object at ...
    """
    language = language.lower()

    # Fallback to English
    if language not in DICTIONARIES:
        language = 'en-us'
    path = os.path.join(
        os.path.dirname(__file__),
        'dicts/%s.dic' % DICTIONARIES[language]
    )
    return Hyphenator(path)


def fix_linebreaks(html):
    return html.replace('</br>', '')


# Test when standalone
def _test():
    """Run doctests"""
    import doctest
    doctest.testmod(verbose=True)


if __name__ == '__main__':
    _test()
