=====
p7doi
=====

.. image:: https://img.shields.io/travis/bfontaine/p7doi.png
   :target: https://travis-ci.org/bfontaine/p7doi
   :alt: Build status

.. image:: https://img.shields.io/coveralls/bfontaine/p7doi/master.png
   :target: https://coveralls.io/r/bfontaine/p7doi?branch=master
   :alt: Coverage status

.. image:: https://img.shields.io/pypi/v/p7doi.png
   :target: https://pypi.python.org/pypi/p7doi
   :alt: Pypi package

.. image:: https://img.shields.io/pypi/dm/p7doi.png
   :target: https://pypi.python.org/pypi/p7doi

**p7doi** is a tool for `Paris 7`_ students who read research papers outside the
university. A lot of them are behind a paywall, which can be bypassed by using
the university’s proxy because it’s subscribed to a bunch of these websites.

Note: you’ll need to login with your student credentials when asked to.

.. _Paris 7: http://www.univ-paris-diderot.fr/english/sc/site.php?bc=accueil&np=accueil&g=m/

Install
-------

.. code-block::

    pip install p7doi

Usage
-----

.. code-block::

    p7doi <doi>

It’ll open the article in your default web browser. Note that you might need to
put the DOI between quotes if it contains characters that could be interpreted
by your shell (e.g. parentheses).

Example
~~~~~~~

.. code-block::

    p7doi 10.1126/science.298.5594.824

Tests
-----

Clone this repo, then: ::

    [sudo] make deps
    make check
