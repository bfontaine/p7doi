# -*- coding: UTF-8 -*-
from __future__ import print_function

import webbrowser
import sys

__version__ = '0.0.1'

DOI_URL = 'http://rproxy.sc.univ-paris-diderot.fr/login' + \
    '?url=http://dx.doi.org/%s'


def open_doi(doi):
    """
    Open the URL for the given DOI in the default browser
    """
    webbrowser.open_new_tab(DOI_URL % doi)


def cli():
    """
    CLI endpoint
    """
    if len(sys.argv) < 2:
        print(u'Usage: %s <doi>' % sys.argv[0])
        return sys.exit(1)

    doi = sys.argv[1]

    if doi.startswith('-'):
        if doi in ['-v', '-version', '--version']:
            print(u'p7doi v%s' % __version__)
        else:
            print(u"Unrecognized option: '%s'" % doi)
            return sys.exit(1)
        return sys.exit(0)

    open_doi(doi)
