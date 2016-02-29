from .latexNotes import LatexNotes

class LatexFormater:
    
    def __init__(self, filepath = ""):
        self._filepath = filepath
        self._content = ""
        
    def __readContent(self, filepath = None):
        if(filepath is not None):
            self._filepath = filepath
            
        with open(self._filepath, "r") as file:
            self._content = file.read()
            
    def format(self, fields):
        if(not self._content):
            print("No content to format, aborted")