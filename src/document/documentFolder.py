# -*- coding: utf-8 -*-

from .documentFields import DocumentFields
from .latexNotes import LatexNotes
from .wikiNotes import WikiNotes
from .notes import Notes
from fs.path import Path
from fs.file import File
from fs.directory import Directory


class DocumentFolder:
    
    VIDEOS_DIR_NAME = "videos"
    IMAGES_DIR_NAME = "images"
    NOTES_DIR_NAME = "notes"
    DESCRIPTION_DIR_NAME = "description"

    INTERN_FOLDERS = [VIDEOS_DIR_NAME, IMAGES_DIR_NAME, NOTES_DIR_NAME, DESCRIPTION_DIR_NAME]
    
    BIBLIODATA_FILE_NAME = "biblio_data"
    
    wordsRemoved = ["a", "an", "and", "of", "on", "the"]
    
    def __init__(self, path=""):
        if (path.__class__ == Path):
            self.path_ = path
        else:
            self.path_ = Path(path)
        self.fields_ = None

    def getDir(self):
        return Directory(self.path_)
        
    def setPath(self, path):
        if (path.__class__ == Path):
            self.path_ = path
        else:
            self.path_ = Path(path)

    def setDocFields(self, fields):
        self.fields_ = fields

    # The name is computed from the title of the document, obtained in the fields.
    def computeFolderName(self):
        # def isAlphaNum(l) : return (l.isalnum() or l.isspace())
        name = ""
        if (self.fields_ != None and self.fields_.hasTitle()):
            title = self.fields_.getField("title")
            title = ''.join(ch for ch in title if ch.isalnum() or ch.isspace())
            words = title.split()
            for i, w in enumerate(words):
                if (w not in self.wordsRemoved): 
                    name += w
                    if (i < len(words)-1):
                        name += "_"
        return name.lower()

    # Creates a document folder in the directory referenced by the given path
    # See the method computeFolderName for more details.
    def create(self, path="."):
        if (self.fields_ == None):
            print("Error : attempt to create a document folder without fields")
            return
        elif (not self.fields_.hasTitle()):
            print("Error : attempt to create a document folder without title")
            return
        
        name = self.computeFolderName()
        self.path_ = Path(path + "/" + name)
        folder = Directory(self.path_)
        folder.createDir()

    def createInternFolder(self, name):
        docDir = Directory(self.path_)

        # TODO : exception
        if (not docDir.exists()):
            print("Unable to create internal folder ", name, " in : ", self.path_)
            return

        dir = Directory(self.path_.getAbsolutePath() + "/" + name)
        dir.createDir()

    def delete(self):
        Directory(self.path_).removeDir()

    def organize(self, filesToMoveIn=None):
        d = Directory(self.path_)
        if (not d.exists()):
            print("Error : attempt to organize a non existing folder : ", self.path_)
            return

        notesPath = self.path_.getAbsolutePath()
        latexNotes = LatexNotes(self.fields_)
        latexNotes.createAllContent()
        latexNotes.writeContent(notesPath)

        wikiNotes = WikiNotes(self.fields_)
        wikiNotes.createAllContent()
        wikiNotes.writeContent(notesPath)

        if(filesToMoveIn is not None):
            for file in filesToMoveIn:
                f = file
                if(type(file) != File):
                    f = File(file)
                f.moveFile(self.path_.getAbsolutePath())

    def getNotesFilePath(self):
        path = self.path_.getAbsolutePath() + "/" + LatexNotes.FILENAME
        return path

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
        
        
        
        
        
    
