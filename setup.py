"""
`pysource-spellchecker` extracts all strings (including unicode
strings) and comments and passes them to the `enchant` spellchecker.
"""

from setuptools import setup, find_packages
additional_keywords ={}

from distutils.core import Command
from distutils import log
import os

setup(
    name = "pysource-spellchecker",
    version = "0.1",
    scripts = ['pypsource-spellchecker'],
    install_requires = ['pyenchant'],

    packages=find_packages(exclude=['ez_setup']),


    # metadata for upload to PyPI
    author = "Hartmut Goebel",
    author_email = "h.goebel@crazy-compiler.com",
    description = "Spellcheck strings and comments in Python source files using Enchant",
    long_description = __doc__,
    license = "GPL 3.0",
    keywords = "pdf poster",
    url          = "https://github.com/htgoebel/pysource-spellchecker",
    download_url = "http://pypi.python.org/pypi/pysource-spellchecker",
    classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Quality Assurance',
    ],

    # these are for easy_install (used by bdist_*)
    zip_safe = True,
)
