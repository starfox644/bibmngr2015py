# -*- coding: utf-8 -*-

from documentFields import DocumentFields
from documentFolder import DocumentFolder
from bibtex.bibtexReader import BibtexReader

# TODO : handle errors when reading bibtex file

class Document:
    def __init__(self):
        self.fields_ = None
        self.folderPath_ = None

    def readFields(self, bibtexPath):
        success = False
        parser = BibtexReader("article.bib")
        fields = parser.read()
        if (fields != None):
            self.fields_ = fields
            success = True
        return success

    def createDocumentFolder(self, folderPath="."):
        self.folderPath_ = folderPath
        if (self.fields_ == None):
            print "Error : attempt to create a document folder without fields at : ", folderPath
            return

        folder = DocumentFolder()
        folder.setDocFields(self.fields_)
        folder.create(folderPath)
        folder.organize()

