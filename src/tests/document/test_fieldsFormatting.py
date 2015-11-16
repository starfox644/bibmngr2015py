# -*- coding: utf-8 -*-

import sys
sys.path.append("../..")

from tests.test import Test
from document.fieldsFormatting import *

class TestFieldsFomatting(Test):
    def __init__(self):
        Test.__init__(self, "FieldsFormatting")
        self.addTestFunction(self.authors)
        self.addTestFunction(self.journal)

    def authors(self):
        authors = "Xue, Su and Agarwala, Aseem and Dorsey, Julie and Rushmeier, Holly"
        newAuthors = "Su Xue, Aseem Agarwala, Julie Dorsey, Holly Rushmeier"
        assert(formatAuthors(authors) == newAuthors)

        authors = "Xue, Su Yang and Agarwala, Aseem J. and Dorsey Lamonde, Julie and Rushmeier, Holly Marie"
        newAuthors = "Su Yang Xue, Aseem J. Agarwala, Julie Dorsey Lamonde, Holly Marie Rushmeier"
        assert(formatAuthors(authors) == newAuthors)

        authors = "Su Yang Xue and Aseem J. Agarwala and Julie Dorsey Lamonde and Holly Marie Rushmeier"
        newAuthors = "Su Yang Xue, Aseem J. Agarwala, Julie Dorsey Lamonde, Holly Marie Rushmeier"
        assert(formatAuthors(authors) == newAuthors)

    def journal(self):
        journal = "ACM trans. on graph."
        newJournal = "ACM Transactions on Graphics"
        result = formatJournal(journal)
        assert(formatJournal(journal) == newJournal)

t = TestFieldsFomatting()
t.runTests()
