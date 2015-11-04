# -*- coding: utf-8 -*-

def strToDocType(typeStr):
    docType = DocumentFields.UNKNOWN
    if (typeStr in DocumentFields.TYPES_STR):
        docType = DocumentFields.TYPES_STR[typeStr]
    return docType

class DocumentFields:

    ARTICLE = 0
    BOOK = 1
    BOOKLET = 2
    CONFERENCE = 3
    INBOOK = 4
    INCOLLECTION = 5
    INPROCEEDINGS = 6
    MANUAL = 7
    MASTERTHESIS = 8
    MISC = 9
    PHDTHESIS = 10
    PROCEEDINGS = 11
    TECHREPORT  = 12
    UNPUBLISHED = 13
    UNKNOWN = 14
    
    TYPES = [
        ARTICLE,
        BOOK,
        BOOKLET,
        CONFERENCE,
        INBOOK,
        INCOLLECTION,
        INPROCEEDINGS,
        MANUAL,
        MASTERTHESIS,
        MISC,
        PHDTHESIS,
        PROCEEDINGS,
        TECHREPORT,
        UNPUBLISHED
    ]

    TYPES_STR = {
        "article":ARTICLE,
        "book":BOOK,
        "booklet":BOOKLET,
        "conference":CONFERENCE,
        "inbook":INBOOK,
        "incollection":INCOLLECTION,
        "inproceedings":INPROCEEDINGS,
        "manual":MANUAL,
        "masterthesis":MASTERTHESIS,
        "misc":MISC,
        "phdthesis":PHDTHESIS,
        "proceedings":PROCEEDINGS,
        "techreport":TECHREPORT,
        "unpublished":UNPUBLISHED
    }
    
    def __init__(self):
        self.type_ = self.UNKNOWN
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
        if (docType != self.UNKNOWN and not docType in self.TYPES):
            print("Warning : incorrect type for document")
            self.type_ = self.UNKNOWN
        else:    
            self.type_ = docType
        
    def __str__(self):
        s = ""
        for field, value in self.fields_.items():
            s += field + " : " + value + "\n"
        return s