# -*- coding: utf-8 -*-

import sys
sys.path.append("../..")

from tests.test import Test

from document.documentFields import DocumentFields
from document.documentFields import strToDocType

class TestDocumentFields(Test):
    def __init__(self):
        Test.__init__(self, "DocumentFields")
        self.addTestFunction(self.createEmpty)
        self.addTestFunction(self.strToDocType)
        self.addTestFunction(self.addField)
        self.addTestFunction(self.getEmptyField)
        self.addTestFunction(self.addMultipleFields)
        self.addTestFunction(self.setType)
        
    def createEmpty(self):
        a = DocumentFields()
        assert (a.getNbFields() == 0)
        assert (a.getDocType() == DocumentFields.UNKNOWN)

    def strToDocType(self):
        fields = DocumentFields
        assert(strToDocType("article") == DocumentFields.ARTICLE)
        assert(strToDocType("book") == DocumentFields.BOOK)
        assert(strToDocType("booklet") == DocumentFields.BOOKLET)
        assert(strToDocType("conference") == DocumentFields.CONFERENCE)
        assert(strToDocType("inbook") == DocumentFields.INBOOK)
        assert(strToDocType("incollection") == DocumentFields.INCOLLECTION)
        assert(strToDocType("inproceedings") == DocumentFields.INPROCEEDINGS)
        assert(strToDocType("manual") == DocumentFields.MANUAL)
        assert(strToDocType("masterthesis") == DocumentFields.MASTERTHESIS)
        assert(strToDocType("misc") == DocumentFields.MISC)
        assert(strToDocType("phdthesis") == DocumentFields.PHDTHESIS)
        assert(strToDocType("proceedings") == DocumentFields.PROCEEDINGS)
        assert(strToDocType("techreport") == DocumentFields.TECHREPORT)
        assert(strToDocType("unpublished") == DocumentFields.UNPUBLISHED)

        assert(strToDocType("other") == DocumentFields.UNKNOWN)
        assert(strToDocType("éèà") == DocumentFields.UNKNOWN)
    
    def addField(self):
        a = DocumentFields()
        a.setField("title", "bc")
        assert (a.getNbFields() == 1)
        assert (a.hasField("title"))
        assert (a.getField("title") == "bc")
        
    def getEmptyField(self):
        a = DocumentFields()
        assert (a.getField("title") == None)
        
    def addMultipleFields(self):
        a = DocumentFields()
        a.setField("title", "bc")
        a.setField("conf", "machin")
        a.setField("author", "martin")
        assert (a.getNbFields() == 3)
        assert (a.hasField("title"))
        assert (a.hasField("conf"))
        assert (a.hasField("author"))
        assert (a.getField("title") == "bc")
        assert (a.getField("conf") == "machin")
        assert (a.getField("author") == "martin")
        
    def setType(self):
        a = DocumentFields()
        
        for t in DocumentFields.TYPES:
            a.setDocType(t)
            assert (a.getDocType() == t)
        
        a.setDocType(DocumentFields.UNKNOWN)
        assert (a.getDocType() == DocumentFields.UNKNOWN)
        
    
t = TestDocumentFields()
t.runTests()