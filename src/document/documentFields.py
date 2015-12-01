# -*- coding: utf-8 -*-

def strToDocType(typeStr):
    docType = DocumentFields.DOC_UNKNOWN
    s = typeStr.lower()
    if (s in DocumentFields.TYPES_STR):
        docType = DocumentFields.TYPES_STR[s]
    return docType

class DocumentFields:

    DOC_ARTICLE = 0
    DOC_BOOK = 1
    DOC_BOOKLET = 2
    DOC_CONFERENCE = 3
    DOC_INBOOK = 4
    DOC_INCOLLECTION = 5
    DOC_INPROCEEDINGS = 6
    DOC_MANUAL = 7
    DOC_MASTERTHESIS = 8
    DOC_MISC = 9
    DOC_PHDTHESIS = 10
    DOC_PROCEEDINGS = 11
    DOC_TECHREPORT  = 12
    DOC_UNPUBLISHED = 13
    DOC_UNKNOWN = 14
    
    TYPES = [
        DOC_ARTICLE,
        DOC_BOOK,
        DOC_BOOKLET,
        DOC_CONFERENCE,
        DOC_INBOOK,
        DOC_INCOLLECTION,
        DOC_INPROCEEDINGS,
        DOC_MANUAL,
        DOC_MASTERTHESIS,
        DOC_MISC,
        DOC_PHDTHESIS,
        DOC_PROCEEDINGS,
        DOC_TECHREPORT,
        DOC_UNPUBLISHED
    ]

    TYPES_STR = {
        "article":DOC_ARTICLE,
        "book":DOC_BOOK,
        "booklet":DOC_BOOKLET,
        "conference":DOC_CONFERENCE,
        "inbook":DOC_INBOOK,
        "incollection":DOC_INCOLLECTION,
        "inproceedings":DOC_INPROCEEDINGS,
        "manual":DOC_MANUAL,
        "masterthesis":DOC_MASTERTHESIS,
        "misc":DOC_MISC,
        "phdthesis":DOC_PHDTHESIS,
        "proceedings":DOC_PROCEEDINGS,
        "techreport":DOC_TECHREPORT,
        "unpublished":DOC_UNPUBLISHED
    }
    
    def __init__(self):
        self.type_ = self.DOC_UNKNOWN
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
        if (docType != self.DOC_UNKNOWN and not docType in self.TYPES):
            print("Warning : incorrect type for document")
            self.type_ = self.DOC_UNKNOWN
        else:    
            self.type_ = docType
        
    def __str__(self):
        s = ""
        for field, value in self.fields_.items():
            s += field + " : " + value + "\n"
        return s