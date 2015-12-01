# -*- coding: utf-8 -*-

import sys
sys.path.append("../..")

import unittest
from unittest import TestCase

from document.documentFields import DocumentFields
from document.documentFields import strToDocType

class TestDocumentFields(TestCase):
        
    def test_createEmpty(self):
        a = DocumentFields()
        assert (a.getNbFields() == 0)
        assert (a.getDocType() == DocumentFields.DOC_UNKNOWN)

    def test_strToDocType(self):
        self.assertEqual(strToDocType("article"),  DocumentFields.DOC_ARTICLE)
        self.assertEqual(strToDocType("Article"),  DocumentFields.DOC_ARTICLE)

        self.assertEqual(strToDocType("book"),  DocumentFields.DOC_BOOK)
        self.assertEqual(strToDocType("Book"),  DocumentFields.DOC_BOOK)

        self.assertEqual(strToDocType("booklet"),  DocumentFields.DOC_BOOKLET)
        self.assertEqual(strToDocType("Booklet"),  DocumentFields.DOC_BOOKLET)

        self.assertEqual(strToDocType("conference"),  DocumentFields.DOC_CONFERENCE)
        self.assertEqual(strToDocType("Conference"),  DocumentFields.DOC_CONFERENCE)

        self.assertEqual(strToDocType("inbook"), DocumentFields.DOC_INBOOK)
        self.assertEqual(strToDocType("InBook"), DocumentFields.DOC_INBOOK)

        self.assertEqual(strToDocType("incollection"), DocumentFields.DOC_INCOLLECTION)
        self.assertEqual(strToDocType("InCollection"), DocumentFields.DOC_INCOLLECTION)

        self.assertEqual(strToDocType("inproceedings"), DocumentFields.DOC_INPROCEEDINGS)
        self.assertEqual(strToDocType("InProceedings"), DocumentFields.DOC_INPROCEEDINGS)

        self.assertEqual(strToDocType("manual"), DocumentFields.DOC_MANUAL)
        self.assertEqual(strToDocType("Manual"), DocumentFields.DOC_MANUAL)

        self.assertEqual(strToDocType("masterthesis"), DocumentFields.DOC_MASTERTHESIS)
        self.assertEqual(strToDocType("MasterThesis"), DocumentFields.DOC_MASTERTHESIS)

        self.assertEqual(strToDocType("misc"), DocumentFields.DOC_MISC)
        self.assertEqual(strToDocType("Misc"), DocumentFields.DOC_MISC)

        self.assertEqual(strToDocType("phdthesis"), DocumentFields.DOC_PHDTHESIS)
        self.assertEqual(strToDocType("PhdThesis"), DocumentFields.DOC_PHDTHESIS)

        self.assertEqual(strToDocType("proceedings"), DocumentFields.DOC_PROCEEDINGS)
        self.assertEqual(strToDocType("Proceedings"), DocumentFields.DOC_PROCEEDINGS)

        self.assertEqual(strToDocType("techreport"), DocumentFields.DOC_TECHREPORT)
        self.assertEqual(strToDocType("TechReport"), DocumentFields.DOC_TECHREPORT)

        self.assertEqual(strToDocType("unpublished"), DocumentFields.DOC_UNPUBLISHED)
        self.assertEqual(strToDocType("Unpublished"), DocumentFields.DOC_UNPUBLISHED)

        self.assertEqual(strToDocType("other"), DocumentFields.DOC_UNKNOWN)
        self.assertEqual(strToDocType("éèà"), DocumentFields.DOC_UNKNOWN)
    
    def test_addField(self):
        a = DocumentFields()
        a.setField("title", "bc")
        self.assertEqual (a.getNbFields(), 1)
        self.assertTrue(a.hasField("title"))
        self.assertEqual(a.getField("title"), "bc")

    def test_changeField(self):
        a = DocumentFields()
        a.setField("title", "bc")
        a.setField("title", "Other")
        self.assertEqual (a.getNbFields(), 1)
        self.assertTrue(a.hasField("title"))
        self.assertEqual(a.getField("title"), "Other")
        
    def test_getEmptyField(self):
        a = DocumentFields()
        self.assertIsNone(a.getField("title"), None)
        
    def test_addMultipleFields(self):
        a = DocumentFields()
        a.setField("title", "bc")
        a.setField("conf", "machin")
        a.setField("author", "martin")
        self.assertEqual (a.getNbFields(), 3)
        self.assertTrue(a.hasField("title"))
        self.assertTrue(a.hasField("conf"))
        self.assertTrue(a.hasField("author"))
        self.assertEqual(a.getField("title"), "bc")
        self.assertEqual(a.getField("conf"), "machin")
        self.assertEqual(a.getField("author"), "martin")
        
    def test_setType(self):
        a = DocumentFields()
        
        for t in DocumentFields.TYPES:
            a.setDocType(t)
            self.assertEqual(a.getDocType(), t)
        
        a.setDocType(DocumentFields.DOC_UNKNOWN)
        self.assertEqual(a.getDocType(), DocumentFields.DOC_UNKNOWN)

if __name__ == '__main__':
    unittest.main()
