**********
nfocleaner
**********

A simple utility to remove art from NFO files.


============
Installation
============

This script depends on:

* Python 3
* `Setuptools <https://pypi.python.org/pypi/setuptools>`_ (for installation only)
* `Click <http://click.pocoo.org/>`_

To install it, just clone the repository and run

.. code-block:: bash

    $python setup.py install


=====
Usage
=====

::

    Usage: nfocleaner [OPTIONS] NFO

    Options:
      -o, --out FILENAME  Output file. Defaults to stdout.
      --help              Show this message and exit.

Supplying ``-`` instead of a filename, ``nfocleaner`` will take input from
stdin.


===========
Description
===========

This script works on the assumption that in most modern (English) NFO files the
art is drawn with non-ASCII characters, while the content is composed entirely
of ASCII characters. Therefore this script will:

* Substitute any non-ASCII character with an ASCII space (' ');
* Strip all trailing whitespace;
* Strip any empty lines at the beginning or at the end of the file;
* Remove any superfluous indentation.
