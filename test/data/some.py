#!/usr/bin/env python2.7
"""
This file is part of pysource-spellchecker.

This word should be in project.dict: ixelbrings
This word should not be in project.dict: mixelmux
"""

# The next line intentionally contains a typo behind the `--` to
# trigger the spell checker.
#!/usr/bin/env python -- dummy shebanG word, will be skipped, too :-(
#!/usr/bin/env perl -- not for python, will not be skipped


# this is a comment
u'This is a unicode string'
'a' # one character
u'\xfc' # one unicode character (u-umlaut)

import lib2to3.main
import argparse

