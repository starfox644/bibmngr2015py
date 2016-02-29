from document.documentFields import DocumentFields
from document.documentFields import strToDocType
from fs.myPath import MyPath

from . import bibtexparser

class BibtexReader:
    
    def __init__(self, bibtexPath):
        self.path = MyPath(bibtexPath)
    
    # reads the file and returns a DocumentFields object
    def read(self):  
        fields = DocumentFields()
        with open(self.path.path) as bibtex_file:
            bibtex_str = bibtex_file.read()
                
        bib_database = bibtexparser.loads(bibtex_str)

        for entry in bib_database.entries:
            for field, value in entry.items():
                if (field == "ENTRYTYPE"):
                    docType = strToDocType(value)
                    fields.setDocType(docType)
                elif (field != "ID"):
                    fields.setField(field, value)
        
        return fields
        