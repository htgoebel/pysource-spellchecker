"""
Spellcheck texts using `enchant`.
"""

import sys

import enchant
from enchant.checker import SpellChecker as _SpellChecker
from enchant.checker.CmdLineChecker import CmdLineChecker
from enchant.tokenize import get_tokenizer
from enchant.tokenize import EmailFilter, URLFilter

__author__ = "Hartmut Goebel <h.goebel@crazy-compilers.com>"
__copyright__ = "Copyright 2012 by Hartmut Goebel <h.goebel@crazy-compilers.com>"
__licence__ = "GNU Public Licence v3 (GPLv3)"


class SpellChecker(object):
    def __init__(self, language, pwl=None):
        if pwl:
            language = enchant.DictWithPWL(language, pwl)
        self._checker = _SpellChecker(lang=language,
                                      filters=[EmailFilter,URLFilter])

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
                                      filters=[EmailFilter,URLFilter])
        self.cmdln = CmdLineChecker()
        self.cmdln.set_checker(self._checker)

    def check(self, text):
        self._checker.set_text(text)
        self.cmdln.run()
        return self._checker.get_text()
