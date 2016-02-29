# -*- coding: utf-8 -*-

import os
from pathlib import PurePath, Path

class MyPath:
    
    def __init__(self, path = ""):
        if(isinstance(path, str)):
            strPath = path
            
        elif(isinstance(path, MyPath)
             or isinstance(path, PurePath)
             or isinstance(path, Path)):
            
            strPath = str(path)
            
        else:
            raise TypeError("path must be of type str or MyPath")
        
        # cleans the path, i.e. removes multiple adjacent '/' and '.'
        self._strPath = str(PurePath(strPath))
        
    
    ##
    #    Returns the absolute path of the file, i.e. from the root of the file system.
    #    Does not produce an exception if the file does not exist.
    #    The '..' directories are kept in the path due to the possible presence of links.
    #    If the path already begins with '/' it is not changed.
    #
    #    @return A string containing the absolute path.
    #    @exception    FileNotFound If the path is not associated to a file.
    #                  RuntimeError If an infinite loop is made during the path resolution.  
    #    
    def getAbsolutePath(self):
        try:
            absPath = Path(self._strPath).resolve()
            absPath = str(absPath)
            
        except FileNotFoundError:
            if(PurePath(self._strPath).is_absolute()):
                absPath = self._strPath
            else:
                absPath = os.path.abspath("") + "/" + self._strPath
            
        return absPath
    
    ##
    #    Returns the path.
    #    The path is clean, i.e. without multiple adjacent '/' and without '.' in the path, unless it is empty.
    #    If the path is empty, '.' is returned.
    #
    def getPath(self):
        return str(PurePath(self._strPath))
    
    ##
    #    Sets the path.
    # 
    def setPath(self, path):
        
        if(isinstance(path, str)):
            strPath = path
            
        elif(isinstance(path, MyPath)
             or isinstance(path, PurePath)
             or isinstance(path, Path)):
            
            strPath = str(path)
            
        else:
            raise TypeError("path must be of type str or MyPath")
        
        self._strPath = strPath
    
    ##
    #     Returns the path without the extension of the file.
    #     For example, returns a/b/c for a/b/c.pdf
    #
    def getPathBasename(self):
        parent = self.parent.path
        
        # don't add ./ when the result is only '.'
        if(parent == '.' and self.basename):
            parent = ""
            
        elif(parent != '.'):
            parent += "/"
        
        return parent + self.basename
    
    ##
    #    Gets the absolute path without the extension.
    #    For example, returns /home/user/a/b/c for a/b/c.pdf
    #
    def getAbsoluteBasename(self):
        absPath = PurePath(self.getAbsolutePath())
        parent = absPath.parent
        absBasename = str(parent) + "/" + PurePath(absPath).stem 
        return str(absBasename)
    
    #
    #     Returns the file name of the path, i.e. the last component.
    #     For example, returns c.pdf for a/b/c.pdf
    def getFilename(self):
        filename = PurePath(self._strPath).name
        return filename 
    
    ##
    #    Returns a path with another filename, i.e. the last component.
    #    For example, MyPath('a/b/c.pdf').withFilename('d.png') returns the path 'a/b/d.png'
    #
    #    @exception ValueError if the name is empty or contains a character '/'
    #
    def withFilename(self, filename):
        if(not isinstance(filename, str)):
            raise TypeError("filename must be of type str")
        
        if(not filename):
            raise ValueError("The filename must not be empty")
        
        if('/' in filename):
            raise ValueError("The filename must not contain '/'")
        
        # if the path is the root, the filename is added
        parent = self.parent.path
        if(self._strPath == "/"):
            parent = ""
        
        newPath = MyPath(parent + "/" + filename)
        return newPath
    
    #
    #     Returns the file name of the path, i.e. the last component without the extension.
    #     For example, returns c for a/b/c.pdf
    #
    def getBasename(self):
        return PurePath(self._strPath).stem
    
    ##
    #    Returns a path with another basename, i.e. the last component.
    #    For example, MyPath('a/b/c.pdf').withBasename('d') returns the path 'a/b/d'
    #
    #    @exception ValueError if the basename is empty or contains a character '/'
    #
    def withBasename(self, basename):
        if(not isinstance(basename, str)):
            raise TypeError("filename must be of type str")
        
        if(not basename):
            raise ValueError("The basename must not be empty")
        
        if('/' in basename):
            raise ValueError("The basename must not contain '/'")
        
        # if the path is the root, the basename is added
        parent = self.parent.path
        if(self._strPath == "/"):
            parent = ""
        
        newPath = MyPath(parent + "/" + basename + self.extension)
        return newPath
    
    ##
    #     Returns the extension at the end of the file, i.e. the part beginning at the last dot.
    #     For example, returns .pdf for a/b/c.pdf
    #    
    def getExtension(self):
        return PurePath(self._strPath).suffix
    
    ##
    #    Returns a path with another extension, i.e. the part beginning at the last dot.
    #    For example, Path('a/b/c.pdf').withExtension('.png') returns the path 'a/b/c.png'
    #
    def withExtension(self, extension):
        if(not isinstance(extension, str)):
            raise TypeError("filename must be of type str")
        
        if('/' in extension):
            raise ValueError("The extension must not contain '/'")
        
        pathBasename = self.pathBasename
        
        if(self._strPath == '.'):
            pathBasename = ""
            
        newPath = MyPath(pathBasename + extension)
        
        return newPath
    
    ##
    #    Return the path corresponding to the parent.
    #    For example, returns a/b for a/b/c.pdf
    def getParent(self):
        
        parent = PurePath(self._strPath).parent
        return MyPath(parent)
    
    def exists(self):
        return Path(self._strPath).exists()
    
    def findNotUsedPath(self):
        i = 1
        basename = self.basename
        path = MyPath(self._strPath)
        
        while(path.exists()):
            path = path.withBasename(basename + "(" + str(i) + ")")
            i += 1
        
        return path
        
    path = property(getPath, setPath)
    filename = property(getFilename)
    basename = property(getBasename)
    pathBasename = property(getPathBasename)
    extension = property(getExtension)
    
    absolutePath = property(getAbsolutePath)
    absoluteBasename = property(getAbsoluteBasename)
    
    parent = property(getParent)
    
    def __str__(self):
        return self.path
    
    def __eq__(self, other):
        
        if(isinstance(other, str)):
            return self.path == other
        
        elif(isinstance(other, MyPath)):
            return self.path == other.path
        
        else:
            return False
    
    
    
    
    
    