.. -*- mode: rst ; ispell-local-dictionary: "american" -*-

==========================
pysource-spellchecker
==========================

-------------------------------------------------------------
spellcheck strings and comments in Python source files
-------------------------------------------------------------

:Author:    Hartmut Goebel <h.goebel@crazy-compilers.com>
:Version:   Version 0.1
:Copyright: 2012 by Hartmut Goebel
:Licence:   GNU Public Licence v3 (GPLv3)
:Homepage:  http://github.com/htgoebel/pysource-spellchecker


`pysource-spellchecker` extracts all strings (including unicode
strings) and comments and passes them to the `enchant` spellchecker.


Usage
~~~~~~~~~~~~~~~~

``pypsource-spellchecker`` <options> source-file ...


Options
--------------------

  -h, --help            show this help message and exit
  --language LANGUAGE   language to use for spellchecking, default: en_US
  --pwl PWL             personal wordlist to use, default: project.dict
  --no-pwl              do not use any personal wordlist.

Mode of operation
'''''''''''''''''''
  --list                simply list all spellchecking errors (this is the
                        default)
  --command-line, --cmd-line, --interactive
                        interactively check the spelling on the command line


Requirements and Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Please note: This package is meant for developers. Even if there are
  some usable examples included, installations instructions are meant
  for developers.

`pysource-spellchecker` requires

* `Python`__ 2.3 or higher (tested with Python 2.6)
* `setuptools`__ or `distribute`__ for installation (see below)
* `PyEnchant`__ (which it self may have additional requirements)

__ http://www.python.org/download/
__ http://pypi.python.org/pypi/setuptools
__ http://pypi.python.org/pypi/distribute
__ http://packages.python.org/pyenchant/


Installing pysource-spellchecker
---------------------------------

Since this package is meant for developers, we assume you have
experience in installing Python packages.

`pysource-spellchecker` is listed on `PyPI (Python Package Index)`__,
so you can install it using `easy_install` or `pip` as usual. Please
refer to the manuals of `easy_install` resp. `pip` for further
information.

__ http://pypi.python.org/pypi

Alternatively you my download and unpack the source package of
`pysource-spellchecker` from
http://pypi.python.org/pypi/pysource-spellchecker and run::

   python ./setup.py install

