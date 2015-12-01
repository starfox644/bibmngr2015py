# -*- coding: utf-8 -*-

import os
import shutil
from .path import Path

class File:
    
    def __init__(self, path=""):
        if (path.__class__ == Path):
            self.path_ = path
        else:
            self.path_ = Path(path)
        
    def getPath(self):
        return self.path_
        
    # Returns true if the file associated to the path exists
    def exists(self):
        return os.path.exists(self.path_.getAbsolutePath())
    
    # Returns true if the file is a regular file, i.e. not a directory
    def isRegularFile(self):
        return os.path.isfile(self.path_.getAbsolutePath())
    
    def isDirectory(self):
        return os.path.isdir(self.path_.getAbsolutePath())
    
    # Creates the file if it does not exist, otherwise does nothing.
    def createFile(self):
        if not self.exists():
            try:
                f = open(self.path_.getAbsolutePath(), 'w')
                f.close()
            except Exception as e:
                print("Unable to create the file ", self.path_, " : ", e)
                
    # Removes the file if it exists
    # If the file is a directory it is not removed
    def removeFile(self):  
        if self.exists() and self.isRegularFile():
            os.remove(self.path_.getAbsolutePath())

    def moveFile(self, newDest):
        shutil.move(self.getPath().getAbsolutePath(), newDest)
        self.path_ = Path(newDest)

    def writeContent(self, content):
        try:
            f = open(self.path_.getAbsolutePath(), 'w')
            f.write(content)
            f.close()
        except Exception as e:
            print("Error : unable to write content in file : ", self.path_, " : ", e)

    def readContent(self):
        content = None
        try:
            f = open(self.path_.getAbsolutePath(), 'r')
            content = f.read()
            f.close()
        except Exception as e:
            print("Error : unable to write content in file : ", self.path_)
        return content
        