# -*- coding: UTF-8 -*-

import platform

if platform.python_version() < '2.7':
    import unittest2 as unittest
else:
    import unittest

import p7doi

class TestP7doi(unittest.TestCase):

    # __version__

    def test_version(self):
        self.assertRegexpMatches(p7doi.__version__, r'^\d+\.\d+\.\d+')
