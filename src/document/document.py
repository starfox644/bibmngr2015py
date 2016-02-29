
from pathlib import Path, PurePath
from fs.myPath import MyPath

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
        
        try:
            fields = parser.read()
        except (OSError, IOError) as e:
            print("Unable to read the bibtex file " + str(bibtexPath) + " : ", e.strerror)
            return False
        
        if (fields != None):
            self.fields_ = fields
            success = True
            
        return success

    def createDocumentFolder(self, bibfilePath, folderPath=None):
        if(folderPath is None):
            bibPath = MyPath(bibfilePath)
            folderPath = str(bibPath.parent)
            
        self.folderPath_ = folderPath
        
        if (self.fields_ == None):
            raise RuntimeError("Error : attempt to create a document folder without fields at : ", self.folderPath_)

        folder = DocumentFolder()
        folder.setDocFields(self.fields_)
        folder.create(folderPath)
        #folder.organize([bibfilePath])
        folder.organize()
        
    def writeLatexNotes(self, path = None):
        if(self.fields_ is not None):
            
            latexNotes = LatexNotes(self.fields_)
            latexNotes.createAllContent()
            
            if(path is None):
                bibPath = MyPath(self.bibtexPath)
                path = str(bibPath.parent)
            
            path = MyPath(path)
            path = path.absoluteBasename
            latexNotes.writeContent(str(path))
            

    def getMinimalFields(self):
        fields = self.fields_
        
        if(fields == None):
            raise RuntimeError("Error : attempt to create a document folder without fields at : ", self.folderPath_)
        
        return None
    
    
    
    
    
    
    

