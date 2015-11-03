# -*- coding: utf-8 -*-

class DocumentFields:
    
    ARTICLE = 0
    BOOK = 1
    THESIS = 2
    SITE = 3
    OTHER = 4
    
    TYPES = [ARTICLE, BOOK, THESIS, SITE]
    
    def __init__(self):
        self.type_ = self.OTHER
        self.fields_ = dict()
        
    def hasField(self, field):
        return field in self.fields_
    
    def setField(self, field, value):
        self.fields_[field] = value
        
    def hasTitle(self):
        return self.hasField("title")
        
    def getField(self, field):
        res = None
        if (self.hasField(field)):
            res = self.fields_[field]
        return res
    
    def getNbFields(self):
        return len(self.fields_)
    
    def getDocType(self):
        return self.type_
    
    def setDocType(self, docType):
        if (docType != self.OTHER and not docType in self.TYPES):
            print "Warning : incorrect type for document"
            self.type_ = self.OTHER
        else:    
            self.type_ = docType
        
    def __str__(self):
        s = ""
        for field, value in self.fields_.iteritems():
            s += field + " : " + value + "\n"
        return s