# -*- coding: utf-8 -*-

import sys
sys.path.append("../..")

from tests.test import Test

from document.documentFields import DocumentFields
from bibtex.bibtexReader import BibtexReader


class TestBibtexReader(Test):
    def __init__(self):
        Test.__init__(self, "BibParser")
        self.addTestFunction(self.writeBib)
        self.addTestFunction(self.parse)
   
    def writeBib(self):
        bib = """@article{Xue:2012:UIR:2185520.2185580,
                author = {Xue, Su and Agarwala, Aseem and Dorsey, Julie and Rushmeier, Holly},
                title = {Understanding and Improving the Realism of Image Composites},
                journal = {ACM Trans. Graph.},
                issue_date = {July 2012},
                volume = {31},
                number = {4},
                month = jul,
                year = {2012},
                issn = {0730-0301},
                pages = {84:1--84:10},
                articleno = {84},
                numpages = {10},
                url = {http://doi.acm.org/10.1145/2185520.2185580},
                doi = {10.1145/2185520.2185580},
                acmid = {2185580},
                publisher = {ACM},
                address = {New York, NY, USA},
                } """
        with open('article.bib', 'w') as bibfile:
            bibfile.write(bib)
   
    def parse(self):
        parser = BibtexReader("article.bib")
        fields = parser.read()
        assert (fields != None)
        assert (fields.getDocType() == DocumentFields.DOC_ARTICLE)
        assert (fields.getField("title") == "Understanding and Improving the Realism of Image Composites")
        assert (fields.getField("journal") == "ACM Trans. Graph.")
        
t = TestBibtexReader()
t.runTests()