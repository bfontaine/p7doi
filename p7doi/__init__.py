# -*- coding: UTF-8 -*-

import sys
import os

DOI_URL = 'http://rproxy.sc.univ-paris-diderot.fr/login?url=http://dx.doi.org/%s'

# note: to be behind P7's proxy, transform an URL like this:
#   http://domain.tld/path
# into:
#   http://domain.tld.rproxy.sc.univ-paris-diderot.fr/path

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'usage: %s <doi>' % sys.argv[0]
        sys.exit(1)

    doi = sys.argv[1]

    os.system("open '%s'" % (DOI_URL % doi,))
