# -*- coding: utf-8 -*-

import os
import shutil
from pathlib import Path

from .myPath import MyPath

class File:
    
    def __init__(self, path=""):
        self._path = MyPath(path)
        self._pythonPath = Path(self._path.path)
        
    def getPath(self):
        return self._path
    
    def setPath(self, path):
        self._path = MyPath(path)
        self._pythonPath = Path(self._path.path)
        
    # Returns true if the file associated to the path exists
    def exists(self):
        return self._pythonPath.exists()
    
    # Returns true if the file is a regular file, i.e. not a directory
    def isRegularFile(self):
        return self._pythonPath.is_file()
    
    def isDirectory(self):
        return self._pythonPath.is_dir()
    
    # Creates the file if it does not exist, otherwise does nothing.
    def createFile(self):
        if not self.exists():
            try:
                f = open(str(self._path), 'w')
                f.close()
            except Exception as e:
                print("Unable to create the file ", self._path, " : ", e)
                
    # Removes the file if it exists
    # If the file is a directory it is not removed
    def removeFile(self):  
        if self.exists() and self.isRegularFile():
            os.remove(str(self._path))

    def moveFile(self, newDest):
        shutil.move(str(self._path), newDest)
        self.setPath(newDest)

    def writeContent(self, content):
        try:
            f = open(str(self._path), 'w')
            f.write(content)
            f.close()
        except Exception as e:
            print("Error : unable to write content to file : ", self._path, " : ", e)

    def readContent(self):
        content = None
        try:
            f = open(str(self._path), 'r')
            content = f.read()
            f.close()
        except Exception as e:
            print("Error : unable to read content from file : ", self._path, ", ", e)
            
        return content
    
    
    
        