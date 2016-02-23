# -*- coding: utf-8 -*-

from document.document import Document
import sys
from tests.test import Test


sys.path.append("../..")


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