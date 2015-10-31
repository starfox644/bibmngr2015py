# -*- coding: utf-8 -*-

import os
import shutil

from path import Path
from file import File
from fileTree import FileTree

# TODO : exceptions instead of print in case of error

class Directory(File):
    
    def __init__(self, path=""):
        File.__init__(self, path)
        
    # creates the directory associated to the path if no file or directory has the same path.
    def createDir(self):
        if (not self.exists()):
            try:
                os.mkdir(self.path_.getAbsolutePath())
            except Exception as e:
                print "Error while creating directory ", self.path_, " : ", e
                
    # creates all the the directories associated to the path            
    def createTree(self):
        if (not self.exists()):
            try:
                os.makedirs(self.path_.getAbsolutePath())
            except Exception as e:
                print "Error while creating directory ", self.path_, " : ", e  
            
    # Removes the directory associated to the path.
    # If the path corresponds to a regular file it is not removed.
    def removeDir(self):
        """

        :rtype :
        """
        if (self.exists() and self.isDirectory()):
            try:
                shutil.rmtree(self.path_.getAbsolutePath())
            except Exception as e:
                print "Error while removing directory ", self.path_, " : ", e
    
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
        content = os.listdir(self.path_.getAbsolutePath())
        absContent = [self.path_.getAbsolutePath() + "/" + c for c in content]
        return set(absContent)

    def containsFolder(self, folderName):
        return (self.path_.getAbsolutePath() + "/" + folderName in self.getDirsList())
                
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