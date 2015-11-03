# -*- coding: utf-8 -*-

import sys
sys.path.append("../..")

from tests.test import Test

from document.documentFields import DocumentFields

class TestDocumentFields(Test):
    def __init__(self):
        Test.__init__(self, "DocumentFields")
        self.addTestFunction(self.createEmpty)
        self.addTestFunction(self.addField)
        self.addTestFunction(self.getEmptyField)
        self.addTestFunction(self.addMultipleFields)
        self.addTestFunction(self.setType)
        
    def createEmpty(self):
        a = DocumentFields()
        assert (a.getNbFields() == 0)
        assert (a.getDocType() == DocumentFields.OTHER)
    
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
        
        a.setDocType(DocumentFields.OTHER)
        assert (a.getDocType() == DocumentFields.OTHER)
        
    
t = TestDocumentFields()
t.runTests()