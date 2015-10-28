from documentFields import DocumentFields
from fs.path import Path
from fs.directory import Directory

class DocumentFolder:
    
    VIDEOS_DIR_NAME = "videos"
    IMAGES_DIR_NAME = "images"
    NOTES_DIR_NAME = "notes"
    DESCRIPTION_DIR_NAME = "description"
    
    BIBLIODATA_FILE_NAME = "biblio_data"
    
    wordsRemoved = ["a", "an", "and", "of", "on", "the"]
    
    def __init__(self, path=""):
        if (type(path) == Path):
            self.path_ = path
        else:
            self.path_ = Path(path)
        self.fields = None

    def getDir(self):
        return Directory(self.path_)
        
    def setPath(self, path):
        if (type(path) == Path):
            self.path_ = path
        else:
            self.path_ = Path(path)

    def setDocFields(self, fields):
        self.fields_ = fields

    # The name is computed from the title of the document, obtained in the fields.
    def computeFolderName(self):
        def isAlphaNum(l) : return (l.isalnum() or l.isspace())
        name = ""
        if (self.fields_ != None and self.fields_.hasTitle()):
            title = self.fields_.getField("title")
            title = filter(isAlphaNum, title)
            words = title.split()
            for i, w in enumerate(words):
                if (w not in self.wordsRemoved): 
                    name += w
                    if (i < len(words)-1):
                        name += "_"
        return name

    # Creates a document folder in the directory referenced by the given path
    # See the method computeFolderName for more details.
    def create(self, path="."):
        if (self.fields_ == None):
            print "Error : attempt to create a document folder without fields"
            return
        elif (not self.fields_.hasTitle()):
            print "Error : attempt to create a document folder without title"
            return
        
        name = self.computeFolderName()
        self.path_ = path + "/" + name
        folder = Directory(self.path_)
        folder.createDir()

    def createInternFolder(self, name):
        docDir = Directory(self.path_)

        # TODO : exception
        if (not docDir.exists()):
            print "Unable to create internal folder ", name, " in : ", self.path_
            return

        dir = Directory(self.path_ + "/" + name)
        dir.createDir()

    def delete(self):
        Directory(self.path_).removeDir()

    def createVideoFolder(self):
        self.createInternFolder(self.VIDEOS_DIR_NAME)

    def createImageFolder(self):
        self.createInternFolder(self.IMAGES_DIR_NAME)

    def createNotesFolder(self):
        self.createInternFolder(self.NOTES_DIR_NAME)

    def createDescFolder(self):
        self.createInternFolder(self.DESCRIPTION_DIR_NAME)
    
    def hasVideoFolder(self):
        return Directory(self.path_).containsFolder(self.VIDEOS_DIR_NAME)

    def hasImageFolder(self):
        return Directory(self.path_).containsFolder(self.IMAGES_DIR_NAME)

    def hasNotesFolder(self):
        return Directory(self.path_).containsFolder(self.NOTES_DIR_NAME)

    def hasDescFolder(self):
        return Directory(self.path_).containsFolder(self.DESCRIPTION_DIR_NAME)
        
        
        
        
        
    
