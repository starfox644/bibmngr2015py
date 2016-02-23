# -*- coding: utf-8 -*-

import os


class Path:
    
    def __init__(self, absolutePath = ""):
        if (absolutePath != ""):
            self.absolutePath_ = os.path.normpath(absolutePath)
            self.absoluteBasename_, self.extension_ = os.path.splitext(self.absolutePath_)
            parts = self.absolutePath_.split("/")
            self.fileName_ = parts.pop()
            self.fileBasename_ = os.path.splitext(self.fileName_)[0]
        else:
            self.absolutePath_ = ""
            self.absoluteBasename_ = ""
            self.fileName_ = ""
            self.fileBasename_ = ""
            self.extension_ = ""
    
    # Returns the absolute path 
    def getAbsolutePath(self):
        return self.absolutePath_
    
    # returns the absolute path without the extension (ex. a/b/c)
    def getAbsoluteBasename(self):
        return self.absoluteBasename_
    
    # returns the file name (ex. c.pdf for file a/b/c.pdf)
    def getFileName(self):
        return self.fileName_
    
    # returns the file basename (ex. c for a/b/c.pdf)
    def getFileBasename(self):
        return self.fileBasename_
    
    # returns the extension at the end of the file, i.e. the part after the last dot
    def getExtension(self):
        return self.extension_
    
    def __str__(self):
        return self.absolutePath_