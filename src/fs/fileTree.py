# -*- coding: utf-8 -*-

import os

from .file import File
from .path import Path


# from directory import *
class FileTree:
    
    def __init__(self, path=""):
        if (type(path) == Path):
            self.path = path
        else:
            self.path = Path(path)
    
    def walkDirs(self, function):
        for root, dirs, files in os.walk(self.path.getAbsolutePath()):
            function(root)
            
    def walkFiles(self, function):
        for root, dirs, files in os.walk(self.path.getAbsolutePath()):
            for f in files:
                function(f)
   
    def walkDirsAndFiles(self, function):
        for root, dirs, files in os.walk(self.path.getAbsolutePath()):
            function(root)
            for f in files:
                function(f)
        
        