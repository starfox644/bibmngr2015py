
from fs.directory import Directory
from fs.file import File
from fs.myPath import MyPath

from document.documentFields import DocumentFields
from document.latexNotes import LatexNotes
from document.notes import Notes
from document.wikiNotes import WikiNotes
from document.infofile import Infofile

class DocumentFolder:
    
    VIDEOS_DIR_NAME = "videos"
    IMAGES_DIR_NAME = "images"
    NOTES_DIR_NAME = "notes"
    DESCRIPTION_DIR_NAME = "description"

    INTERN_FOLDERS = [VIDEOS_DIR_NAME, IMAGES_DIR_NAME, NOTES_DIR_NAME, DESCRIPTION_DIR_NAME]
    
    BIBLIODATA_FILE_NAME = "biblio_data"
    
    wordsRemoved = ["a", "an", "at", "and", "in", "of", "on", "the"]
    
    def __init__(self, path="", fields=None):
        
        if(isinstance(path, MyPath)):
            self._path = path
        else:
            self._path = MyPath(path)
            
        if(fields is None):
            fields = DocumentFields()
            
        self._fields = fields
        self._directory = Directory(self._path)

    def getDirectory(self):
        return self._directory
        
    def getPath(self):
        return self._path
        
    def setPath(self, path):
        if (path.__class__ == MyPath):
            self._path = path
        else:
            self._path = MyPath(path)

    def getDocFields(self, fields):
        return self._fields

    def setDocFields(self, fields):
        self._fields = fields
        
    path = property(getPath, setPath)
        
    def _checkDirectoryExists(self):
        if not self._directory.exists():
            raise IOError("Document directory does not exist anymore")

    # The name is computed from the title of the document, obtained in the fields.
    def computeFolderName(self):
        name = ""
        if (self._fields.hasTitle()):
            title = self._fields.getField("title")
            title = ''.join(ch for ch in title if ch.isalnum() or ch.isspace())
            words = title.split()
            for i, w in enumerate(words):
                if (w not in self.wordsRemoved): 
                    name += w
                    if (i < len(words)-1):
                        name += "_"
            name = name.lower()
            
        return name

    # Creates a document folder in the directory referenced by the given path
    # See the method computeFolderName for more details.
    def create(self, path="."):
        if (not self._fields.hasTitle()):
            raise RuntimeError("Error : attempt to create a document folder without title")
            return
        
        name = self.computeFolderName()
        self._path = MyPath(path + "/" + name)
        self._path = self._path.findNotUsedPath()
        folder = Directory(self._path)
        folder.createDir()
        
    def containsDocumentFiles(self):
        self._checkDirectoryExists()

    def createInternFolder(self, name):
        self._checkDirectoryExists()
        
        directory = Directory(self._path.getAbsolutePath() + "/" + name)
        directory.createDir()
        
    def delete(self):
        Directory(self._path).removeDir()
        
    def readInfos(self):
        self._checkDirectoryExists()
        
        infofile = Infofile()
        success = infofile.readContent(self.infofilePath())
        
        files = self._directory.getContentList()
        
        if(success):
            print("title : ", infofile.title)
            print("Files : ")
            for f in files:  
                print(MyPath(f).filename)
        
    def organize(self, filesToMoveIn=None):
        self._checkDirectoryExists()

        notesPath = self._path.getAbsolutePath()
        latexNotes = LatexNotes(self._fields)
        latexNotes.createAllContent()
        latexNotes.writeContent(notesPath)
        
        title = self._fields.getField("title")
        infofile = Infofile()
        infofile.title = title
        infofile.writeContent(self.infofilePath())

        if(filesToMoveIn is not None):
            for file in filesToMoveIn:
                f = file
                if(type(file) != File):
                    f = File(file)
                f.moveFile(self._path.getAbsolutePath())

    def getNotesFilePath(self):
        path = self._path.getAbsolutePath() + "/" + LatexNotes.FILENAME
        return path
    
    def infofilePath(self):
        return MyPath(self._path.path + "/" + "info")

    def createVideoFolder(self):
        self.createInternFolder(self.VIDEOS_DIR_NAME)

    def createImageFolder(self):
        self.createInternFolder(self.IMAGES_DIR_NAME)

    def createNotesFolder(self):
        self.createInternFolder(self.NOTES_DIR_NAME)

    def createDescFolder(self):
        self.createInternFolder(self.DESCRIPTION_DIR_NAME)
    
    def hasVideoFolder(self):
        self._checkDirectoryExists()
        return Directory(self._path).containsFolder(self.VIDEOS_DIR_NAME)

    def hasImageFolder(self):
        self._checkDirectoryExists()
        return Directory(self._path).containsFolder(self.IMAGES_DIR_NAME)

    def hasNotesFolder(self):
        self._checkDirectoryExists()
        return Directory(self._path).containsFolder(self.NOTES_DIR_NAME)

    def hasDescFolder(self):
        self._checkDirectoryExists()
        return Directory(self._path).containsFolder(self.DESCRIPTION_DIR_NAME)
        
        
        
        
        
    
