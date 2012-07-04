"""
Spellcheck texts using `enchant`.
"""

import sys
import re

import enchant
from enchant.checker import SpellChecker as _SpellChecker
from enchant.checker.CmdLineChecker import CmdLineChecker
from enchant.tokenize import get_tokenizer
from enchant.tokenize import Filter, EmailFilter, URLFilter

__author__ = "Hartmut Goebel <h.goebel@crazy-compilers.com>"
__copyright__ = "Copyright 2012 by Hartmut Goebel <h.goebel@crazy-compilers.com>"
__licence__ = "GNU Public Licence v3 (GPLv3)"


class SheBangFilter(Filter):
    """Filter skipping over shebang lines for the python interpreter.
    This filter skips any words matching the following regular expression:

           ^#!/.+python.*$
    """
    _pattern = re.compile(r"^#!/.+$")
    def _skip(self,word):
        if self._pattern.match(word):
            return True
        return False


filters_to_use = [EmailFilter,URLFilter,SheBangFilter]

class SpellChecker(object):
    def __init__(self, language, pwl=None):
        if pwl:
            language = enchant.DictWithPWL(language, pwl)
        self._checker = _SpellChecker(lang=language,
                                      filters=filters_to_use)

    def check(self, text):
        self._checker.set_text(text)
        for err in self._checker:
            print err.word, '==>', err.suggest()
        return text


class CmdLineSpellChecker(object):
    def __init__(self, language, pwl=None):
        if pwl:
            language = enchant.DictWithPWL(language, pwl)
        self._checker = _SpellChecker(lang=language,
                                      filters=filters_to_use)
        self.cmdln = CmdLineChecker()
        self.cmdln.set_checker(self._checker)

    def check(self, text):
        self._checker.set_text(text)
        self.cmdln.run()
        return self._checker.get_text()
