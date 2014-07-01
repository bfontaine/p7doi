# -*- coding: UTF-8 -*-
from __future__ import print_function

import webbrowser
import sys

__version__ = '0.0.1'

DOI_URL = 'http://rproxy.sc.univ-paris-diderot.fr/login' + \
    '?url=http://dx.doi.org/%s'


def make_doi_url(doi):
    """
    Return an URL for the given DOI
    """
    return DOI_URL % doi


def open_url(url):
    """
    Open an URL in the default browser, in a new tab if possible
    """
    webbrowser.open_new_tab(url)


def open_doi(doi):
    """
    Open the URL for the given DOI in the default browser
    """
    open_url(make_doi_url(doi))


def cli():
    """
    CLI endpoint
    """
    if len(sys.argv) < 2:
        print('Usage: %s <doi>' % sys.argv[0])
        sys.exit(1)

    doi = sys.argv[1]

    if doi.startswith('-'):
        if doi in ['-v', '-version', '--version']:
            print('p7doi v%s' % __version__)
        else:
            print("Unrecognized option: '%s'" % doi)
            sys.exit(1)
        sys.exit(0)

    open_doi(doi)
