# -*- coding: UTF-8 -*-

import platform

if platform.python_version() < '2.7':
    from StringIO import StringIO
    import unittest2 as unittest
else:
    from io import StringIO
    import unittest

import webbrowser
import p7doi
from p7doi import sys

class TestP7doi(unittest.TestCase):

    def setUp(self):
        self.wb_args = None
        def fake_open_new_tab(*args):
            self.wb_args = args

        self.exit_status = None
        def fake_exit(s):
            self.exit_status = s

        self._open_new_tab = webbrowser.open_new_tab
        self._argv = sys.argv
        self._stdout = sys.stdout
        self._exit = sys.exit
        self._version = p7doi.__version__
        sys.stdout = StringIO()
        sys.exit = fake_exit
        webbrowser.open_new_tab = fake_open_new_tab

    def tearDown(self):
        sys.argv = self._argv
        sys.stdout = self._stdout
        sys.exit = self._exit
        p7doi.__version__ = self._version
        webbrowser.open_new_tab = self._open_new_tab

    # __version__

    def test_version(self):
        self.assertRegexpMatches(p7doi.__version__, r'^\d+\.\d+\.\d+')

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

    def test_cli_not_enough_args(self):
        sys.argv = ['xyz']
        p7doi.cli()
        sys.stdout.seek(0)
        self.assertSequenceEqual('Usage: xyz <doi>\n', sys.stdout.read())
        self.assertEquals(1, self.exit_status)

    def test_cli_version_short_flag(self):
        sys.argv = ['xyz', '-v']
        p7doi.__version__ = 'foobar42'
        p7doi.cli()
        sys.stdout.seek(0)
        self.assertSequenceEqual('p7doi vfoobar42\n', sys.stdout.read())
        self.assertEquals(0, self.exit_status)

    def test_cli_version_long_flag1(self):
        sys.argv = ['xyz', '-version']
        p7doi.__version__ = 'f42'
        p7doi.cli()
        sys.stdout.seek(0)
        self.assertSequenceEqual('p7doi vf42\n', sys.stdout.read())
        self.assertEquals(0, self.exit_status)

    def test_cli_version_long_flag2(self):
        sys.argv = ['xyz', '--version']
        p7doi.__version__ = '1xyz'
        p7doi.cli()
        sys.stdout.seek(0)
        self.assertSequenceEqual('p7doi v1xyz\n', sys.stdout.read())
        self.assertEquals(0, self.exit_status)

    def test_cli_version_unrecognized_option(self):
        sys.argv = ['xyz', '-x']
        p7doi.cli()
        sys.stdout.seek(0)
        self.assertSequenceEqual("Unrecognized option: '-x'\n", sys.stdout.read())
        self.assertEquals(1, self.exit_status)
