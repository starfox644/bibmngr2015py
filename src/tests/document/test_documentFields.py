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
        assert (a.getDocType() == DocumentFields.UNKNOWN)

    def test_strToDocType(self):
        self.assertEqual(strToDocType("article"),  DocumentFields.ARTICLE)
        self.assertEqual(strToDocType("Article"),  DocumentFields.ARTICLE)

        self.assertEqual(strToDocType("book"),  DocumentFields.BOOK)
        self.assertEqual(strToDocType("Book"),  DocumentFields.BOOK)

        self.assertEqual(strToDocType("booklet"),  DocumentFields.BOOKLET)
        self.assertEqual(strToDocType("Booklet"),  DocumentFields.BOOKLET)

        self.assertEqual(strToDocType("conference"),  DocumentFields.CONFERENCE)
        self.assertEqual(strToDocType("Conference"),  DocumentFields.CONFERENCE)

        self.assertEqual(strToDocType("inbook"), DocumentFields.INBOOK)
        self.assertEqual(strToDocType("InBook"), DocumentFields.INBOOK)

        self.assertEqual(strToDocType("incollection"), DocumentFields.INCOLLECTION)
        self.assertEqual(strToDocType("InCollection"), DocumentFields.INCOLLECTION)

        self.assertEqual(strToDocType("inproceedings"), DocumentFields.INPROCEEDINGS)
        self.assertEqual(strToDocType("InProceedings"), DocumentFields.INPROCEEDINGS)

        self.assertEqual(strToDocType("manual"), DocumentFields.MANUAL)
        self.assertEqual(strToDocType("Manual"), DocumentFields.MANUAL)

        self.assertEqual(strToDocType("masterthesis"), DocumentFields.MASTERTHESIS)
        self.assertEqual(strToDocType("MasterThesis"), DocumentFields.MASTERTHESIS)

        self.assertEqual(strToDocType("misc"), DocumentFields.MISC)
        self.assertEqual(strToDocType("Misc"), DocumentFields.MISC)

        self.assertEqual(strToDocType("phdthesis"), DocumentFields.PHDTHESIS)
        self.assertEqual(strToDocType("PhdThesis"), DocumentFields.PHDTHESIS)

        self.assertEqual(strToDocType("proceedings"), DocumentFields.PROCEEDINGS)
        self.assertEqual(strToDocType("Proceedings"), DocumentFields.PROCEEDINGS)

        self.assertEqual(strToDocType("techreport"), DocumentFields.TECHREPORT)
        self.assertEqual(strToDocType("TechReport"), DocumentFields.TECHREPORT)

        self.assertEqual(strToDocType("unpublished"), DocumentFields.UNPUBLISHED)
        self.assertEqual(strToDocType("Unpublished"), DocumentFields.UNPUBLISHED)

        self.assertEqual(strToDocType("other"), DocumentFields.UNKNOWN)
        self.assertEqual(strToDocType("éèà"), DocumentFields.UNKNOWN)
    
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
        
        a.setDocType(DocumentFields.UNKNOWN)
        self.assertEqual(a.getDocType(), DocumentFields.UNKNOWN)

if __name__ == '__main__':
    unittest.main()
