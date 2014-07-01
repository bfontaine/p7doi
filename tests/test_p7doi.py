# -*- coding: UTF-8 -*-

import platform

if platform.python_version() < '2.7':
    import unittest2 as unittest
else:
    import unittest

import sys
import webbrowser
import p7doi

class TestP7doi(unittest.TestCase):

    def setUp(self):
        self.wb_args = None
        def fake_open_new_tab(*args):
            self.wb_args = args

        self._open_new_tab = webbrowser.open_new_tab
        self._argv = sys.argv
        webbrowser.open_new_tab = fake_open_new_tab

    def tearDown(self):
        sys.argv = self._argv
        webbrowser.open_new_tab = self._open_new_tab

    # __version__

    def test_version(self):
        self.assertRegexpMatches(p7doi.__version__, r'^\d+\.\d+\.\d+')

    # make_doi_url

    def test_make_doi_url(self):
        self.assertEquals(
            'http://rproxy.sc.univ-paris-diderot.fr/login?url=http://dx.doi.org/10xyz/42.12',
            p7doi.make_doi_url('10xyz/42.12'))

    # open_url

    def test_open_url(self):
        url = 'http://example.com?some=pa&ra=meter'
        p7doi.open_url(url)
        self.assertSequenceEqual([url], self.wb_args)

    # open_doi

    def test_open_doi(self):
        p7doi.open_doi('xyz/abc/10/42.foo')
        self.assertSequenceEqual([
            'http://rproxy.sc.univ-paris-diderot.fr/login?url=http://dx.doi.org/xyz/abc/10/42.foo'
        ], self.wb_args)

    # cli

    def test_cli_doi(self):
        sys.argv = ['p7doi', 'abcd-1234']
        p7doi.cli()
        self.assertSequenceEqual([
            'http://rproxy.sc.univ-paris-diderot.fr/login?url=http://dx.doi.org/abcd-1234'
        ], self.wb_args)
