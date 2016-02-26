# -*- coding: utf-8 -*-

from pathlib import Path, PurePath

from bibtex.bibtexReader import BibtexReader

from .documentFolder import DocumentFolder
from .latexNotes import LatexNotes

# TODO : handle errors when reading bibtex file
class Document:

    DOCUMENT_MINIMAL_FIELDS = "type", "author", "year"

    def __init__(self):
        self.fields_ = None
        self.folderPath_ = None
        self.bibtexPath = None

    def readFields(self, bibtexPath):
        success = False
        self.bibtexPath = bibtexPath
        parser = BibtexReader(bibtexPath)
        fields = parser.read()
        if (fields != None):
            self.fields_ = fields
            success = True
        return success

    def createDocumentFolder(self, bibfilePath, folderPath=None):
        if(folderPath is None):
            bibPath = Path(bibfilePath)
            folderPath = str(bibPath.parent)
            
        self.folderPath_ = folderPath
        if (self.fields_ == None):
            print("Error : attempt to create a document folder without fields at : ", folderPath)
            return

        folder = DocumentFolder()
        folder.setDocFields(self.fields_)
        folder.create(folderPath)
        folder.organize([bibfilePath])
        
    def writeLatexNotes(self, path = None):
        if(self.fields_ is not None):
            
            latexNotes = LatexNotes(self.fields_)
            latexNotes.createAllContent()
            
            if(path is None):
                bibPath = Path(self.bibtexPath)
                path = str(bibPath.parent)
            
            path = Path(path)
            path = path.resolve()
            latexNotes.writeContent(str(path))
            

    def getMinimalFields(self):
        fields = self.fields_
        if(fields == None):
            print("Error : trying to get minimal fields without a field object")
        return None
    
    
    
    
    
    
    

