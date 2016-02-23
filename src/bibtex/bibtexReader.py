from document.documentFields import DocumentFields
from document.documentFields import strToDocType
from fs.path import Path
import sys

from . import bibtexparser


# -*- coding: utf-8 -*-
sys.path.append("../..")

        
class BibtexReader:
    
    def __init__(self, bibtexPath):
        self.path = Path(bibtexPath)
    
    # reads the file and returns a DocumentFields object
    def read(self):  
        fields = DocumentFields()
        try:
            with open(self.path.getAbsolutePath()) as bibtex_file:
                bibtex_str = bibtex_file.read()
        except Exception as e:
            print("Unable to load the bibtex file ", self.path.getAbsolutePath(), " : ", e)
            return None
                
        bib_database = bibtexparser.loads(bibtex_str)

        for entry in bib_database.entries:
            for field, value in entry.items():
                if (field == "ENTRYTYPE"):
                    docType = strToDocType(value)
                    fields.setDocType(docType)
                elif (field != "ID"):
                    fields.setField(field, value)
        
        return fields
        