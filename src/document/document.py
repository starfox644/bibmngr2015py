# -*- coding: utf-8 -*-

from .documentFields import DocumentFields
from .documentFolder import DocumentFolder
from bibtex.bibtexReader import BibtexReader

# TODO : handle errors when reading bibtex file

class Document:

    DOCUMENT_MINIMAL_FIELDS = "type", "author", "year"

    def __init__(self):
        self.fields_ = None
        self.folderPath_ = None

    def readFields(self, bibtexPath):
        success = False
        parser = BibtexReader(bibtexPath)
        fields = parser.read()
        if (fields != None):
            self.fields_ = fields
            success = True
        return success

    def createDocumentFolder(self, bibfilePath, folderPath="."):
        self.folderPath_ = folderPath
        if (self.fields_ == None):
            print("Error : attempt to create a document folder without fields at : ", folderPath)
            return

        folder = DocumentFolder()
        folder.setDocFields(self.fields_)
        folder.create(folderPath)
        folder.organize([bibfilePath])

    def getMinimalFields(self):
        fields = self.fields_
        if(fields == None):
            print("Error : trying to get minimal fields without a field object")
            return None

