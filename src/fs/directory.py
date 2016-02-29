# -*- coding: utf-8 -*-

import os
import shutil
from pathlib import Path

from .file import File
from .fileTree import FileTree
from .myPath import MyPath


# TODO : exceptions instead of print in case of error
class Directory(File):
    
    def __init__(self, path=""):
        File.__init__(self, path)
        
    # creates the directory associated to the path if no file or directory has the same path.
    def createDir(self):
        try:
            self._pythonPath.mkdir(parents=False)
        except FileExistsError:
            None
                
    # creates all the the directories associated to the path            
    def createTree(self):
        try:
            self._pythonPath.mkdir(parents=True)
        except FileExistsError:
            None
            
    # Removes the directory associated to the path.
    # If the path corresponds to a regular file it is not removed.
    def removeDir(self):
        if (self.exists() and self.isDirectory()):
            try:
                shutil.rmtree(self._path.path)
            except OSError as e:
                print("Error while removing directory ", self._path, " : ", e)  
                raise e
    
    # def _addToFiles(self, file):
    #     if (file != self.path_.getAbsolutePath()):
    #         path = Path(file)
    #         self.files_.append(path.getFileName())
            
    def getDirsList(self):
        
        def isDir(d): return File(d).isDirectory()
        
        return set(filter(isDir, self.getContentList()))
    
    def getFilesList(self):
        
        def isFile(d): return File(d).isRegularFile()
        
        return set(filter(isFile, self.getContentList()))
    
    def getContentList(self):
        content = os.listdir(str(self._path))
        absContent = [str(self._path) + "/" + c for c in content]
        return set(absContent)

    def containsFolder(self, folderName):
        return (self._path.path + "/" + folderName in self.getDirsList())
    
    def containsFileExtension(self, extension):
        
        def hasExtension(p): return MyPath(p).extension == extension
        
        res = False
        for file in self.getContentList():
            res |= hasExtension(file)
                
        return res
        
# Creates a file or a directory corresponding to the path.
# If the path corresponds to a directory an object of type Directory is returned, otherwise a File is returned.
# If the path is not associated to a path None is returned.
def createFileOrDir(path):
    f = None
    if os.path.isdir(path):    
        f = Directory(path)
    elif os.path.isfile(path):
        f = File(path)
    return f


