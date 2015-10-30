# -*- coding: utf-8 -*-

import sys
sys.path.append("../..")

from document.document import Document
from tests.test import Test

class TestDocument(Test):
    def __init__(self):
        Test.__init__(self, "Document")
        self.addTestFunction(self.createFolderFromBibfile)

    def createFolderFromBibfile(self):
        doc = Document()
        doc.readFields("article.bib")
        doc.createDocumentFolder()

t = TestDocument()
t.runTests()