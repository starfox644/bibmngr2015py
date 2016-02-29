#! /usr/bin/python3.5

import sys
sys.path.append("../../src")

import os
from fs.myPath import MyPath
from unittest import TestCase
import unittest

class TestMyPath(TestCase):
    
    def setUp(self):
        self.emptyPath = "."
        self.basename = "file"
        self.extension = ".pdf"
        self.filename = "file.pdf"
        
        self.backLocalDir = "a/b/c/../cd" 
        self.backLocalFilename = self.backLocalDir + "/" + self.filename
        self.backLocalBasename = self.backLocalDir + "/" + self.basename
        
        self.localDir = "a/b/cd"
        self.localFilename = self.localDir + "/" + self.filename
        self.localBasename = self.localDir + "/" + self.basename
        
        self.absoluteFile = os.path.abspath("") + "/" + self.filename
        self.absoluteBasename = os.path.abspath("") + "/" + self.basename
        
        self.absoluteDir = os.path.abspath("") + "/" + self.localDir
        self.absoluteDirFile = self.absoluteDir + "/" + self.filename
        self.absoluteDirBasename = self.absoluteDir + "/" + self.basename
        
        self.absoluteBackDir = os.path.abspath("") + "/" + self.backLocalDir
        self.absoluteBackDirFile = self.absoluteBackDir + "/" + self.filename
        self.absoluteBackDirBasename = self.absoluteBackDir + "/" + self.basename
        
        self.otherExtension = ".png"
        self.otherBasename = "image"
        
        self.changedFilename = "image.png"
        self.changedExtension = "file.png"
        self.changedBasename = "image.pdf"
        
        self.localChangedFilename = self.localDir + "/" + self.changedFilename
        self.localChangedBasename = self.localDir + "/" + self.changedBasename
        self.localChangedExtension = self.localDir + "/" + self.changedExtension
        
    
    def test_pathProperty(self):
        
        #=======================================================================
        #     Empty
        #=======================================================================
        
        p = MyPath()
        self.assertEqual(p.path, self.emptyPath, "Empty path must be '.'")
        
        p = MyPath()
        p.path = ""
        self.assertEqual(p.path, self.emptyPath, "Empty path must be '.'")
        
        p = MyPath(".")
        self.assertEqual(p.path, self.emptyPath, "Empty path must be '.'")
        
        p = MyPath()
        p.path = "."
        self.assertEqual(p.path, self.emptyPath, "Empty path must be '.'")
        
        #=======================================================================
        #     Filename
        #=======================================================================
        
        p = MyPath(self.filename)
        self.assertEqual(p.path, self.filename, "Path must not be changed")
        
        p = MyPath()
        p.path = self.filename
        self.assertEqual(p.path, self.filename, "Path must not be changed")
        
        #=======================================================================
        #     Local
        #=======================================================================
        
        p = MyPath(self.localFilename)
        self.assertEqual(p.path, self.localFilename, "Path must not be changed")
        
        p = MyPath()
        p.path = self.localFilename
        self.assertEqual(p.path, self.localFilename, "Path must not be changed")
        
        #=======================================================================
        #     Local with back
        #=======================================================================
        
        p = MyPath(self.backLocalFilename)
        self.assertEqual(p.path, self.backLocalFilename, "Path must not be changed")
        
        p = MyPath()
        p.path = self.backLocalFilename
        self.assertEqual(p.path, self.backLocalFilename, "Path must not be changed")
        
        #=======================================================================
        #     Absolute
        #=======================================================================
        
        p = MyPath(self.absoluteFile)
        self.assertEqual(p.path, self.absoluteFile, "Path must not be changed")
        
        p = MyPath()
        p.path = self.absoluteFile
        self.assertEqual(p.path, self.absoluteFile, "Path must not be changed")
    
    def test_getFilename(self):
        
        #=======================================================================
        #     Empty
        #=======================================================================
        
        p = MyPath()
        
        p.path = ""
        self.assertEqual(p.filename, "", "Filename must be empty")
        
        p.path = "."
        self.assertEqual(p.basename, "", "Filename must be empty")
        
        #=======================================================================
        #     Filename
        #=======================================================================
        
        p.path = self.filename
        self.assertEqual(p.filename, self.filename, "Incorrect Filename")
        
        #=======================================================================
        #     Local
        #=======================================================================
        
        p.path = self.localFilename
        self.assertEqual(p.filename, self.filename, "Incorrect Filename")
        
        #=======================================================================
        #     Local with back
        #=======================================================================
        
        p.path = self.backLocalFilename
        self.assertEqual(p.filename, self.filename, "Incorrect Filename")
        
        #=======================================================================
        #     Absolute
        #=======================================================================
        
        p.path = self.absoluteFile
        self.assertEqual(p.filename, self.filename, "Incorrect Filename")
        
    def test_getBasename(self):
        
        #=======================================================================
        #     Empty
        #=======================================================================
        
        p = MyPath()
        
        p.path = ""
        self.assertEqual(p.basename, "", "Basename must be empty")
        
        p.path = "."
        self.assertEqual(p.basename, "", "Basename must be empty")
        
        #=======================================================================
        #     Filename
        #=======================================================================
        
        p.path = self.filename
        self.assertEqual(p.basename, self.basename, "Incorrect basename")
        
        #=======================================================================
        #     Local
        #=======================================================================
        
        p.path = self.localFilename
        self.assertEqual(p.basename, self.basename, "Incorrect basename")
        
        #=======================================================================
        #     Local with back
        #=======================================================================
        
        p.path = self.backLocalFilename
        self.assertEqual(p.basename, self.basename, "Incorrect basename")
        
        #=======================================================================
        #     Absolute
        #=======================================================================
        
        p.path = self.absoluteFile
        self.assertEqual(p.basename, self.basename, "Incorrect basename")
        
    def test_getAbsolutePath(self):
        
        #=======================================================================
        #     Empty
        #=======================================================================
        
        p = MyPath()
        
        p.path = ""
        self.assertEqual(p.absolutePath, os.path.abspath(""), "Incorrect absolute path")
        
        p.path = "."
        self.assertEqual(p.absolutePath, os.path.abspath(""), "Incorrect absolute path")
        
        #=======================================================================
        #     Filename
        #=======================================================================
        
        p.path = self.filename
        self.assertEqual(p.absolutePath, self.absoluteFile, "Incorrect absolute path")
        
        #=======================================================================
        #     Local
        #=======================================================================
        
        p.path = self.localFilename
        self.assertEqual(p.absolutePath, self.absoluteDirFile, "Incorrect absolute path")
        
        #=======================================================================
        #     Local with back
        #=======================================================================
        
        p.path = self.backLocalFilename
        self.assertEqual(p.absolutePath, self.absoluteBackDirFile, "Incorrect absolute path")
        
        #=======================================================================
        #     Absolute
        #=======================================================================
        
        p.path = self.absoluteFile
        self.assertEqual(p.absolutePath, self.absoluteFile, "Incorrect absolute path")
        
        #=======================================================================
        #     Absolute Dir
        #=======================================================================
        
        p.path = self.absoluteDirFile
        self.assertEqual(p.absolutePath, self.absoluteDirFile, "Incorrect absolute path")
        
    def test_getPathBasename(self):
        
        #=======================================================================
        #     Empty
        #=======================================================================
        
        p = MyPath()
        
        p.path = ""
        self.assertEqual(p.pathBasename, ".", "Incorrect path basename")
        
        p.path = "."
        self.assertEqual(p.pathBasename, ".", "Incorrect path basename")
        
        #=======================================================================
        #     Filename
        #=======================================================================
        
        p.path = self.filename
        self.assertEqual(p.pathBasename, self.basename, "Incorrect path basename")
        
        #=======================================================================
        #     Local
        #=======================================================================
        
        p.path = self.localFilename
        self.assertEqual(p.pathBasename, self.localBasename, "Incorrect path basename")
        
        #=======================================================================
        #     Local with back
        #=======================================================================
        
        p.path = self.backLocalFilename
        self.assertEqual(p.pathBasename, self.backLocalBasename, "Incorrect path basename")
        
        #=======================================================================
        #     Absolute
        #=======================================================================
        
        p.path = self.absoluteFile
        self.assertEqual(p.pathBasename, self.absoluteBasename, "Incorrect path basename")
        
        #=======================================================================
        #     Absolute Dir
        #=======================================================================
        
        p.path = self.absoluteDirFile
        self.assertEqual(p.pathBasename, self.absoluteDirBasename, "Incorrect path basename")
        
    def test_getAbsoluteBasename(self):
        
        #=======================================================================
        #     Empty
        #=======================================================================
        
        p = MyPath()
        
        p.path = ""
        self.assertEqual(p.absoluteBasename, os.path.abspath(""), "Incorrect absolute basename")
        
        p.path = "."
        self.assertEqual(p.absoluteBasename, os.path.abspath(""), "Incorrect absolute basename")
        
        #=======================================================================
        #     Filename
        #=======================================================================
        
        p.path = self.filename
        self.assertEqual(p.absoluteBasename, self.absoluteBasename, "Incorrect absolute basename")
        
        #=======================================================================
        #     Local
        #=======================================================================
        
        p.path = self.localFilename
        self.assertEqual(p.absoluteBasename, self.absoluteDirBasename, "Incorrect absolute basename")
        
        #=======================================================================
        #     Local with back
        #=======================================================================
        
        p.path = self.backLocalFilename
        self.assertEqual(p.absoluteBasename, self.absoluteBackDirBasename, "Incorrect absolute basename")
        
        #=======================================================================
        #     Absolute
        #=======================================================================
        
        p.path = self.absoluteFile
        self.assertEqual(p.absoluteBasename, self.absoluteBasename, "Incorrect absolute basename")
        
        #=======================================================================
        #     Absolute Dir
        #=======================================================================
        
        p.path = self.absoluteDirFile
        self.assertEqual(p.absoluteBasename, self.absoluteDirBasename, "Incorrect absolute basename")
    
    def test_getExtension(self):
        
        
        #=======================================================================
        #     Empty
        #=======================================================================
        
        p = MyPath()
        
        p.path = ""
        self.assertEqual(p.extension, "", "Incorrect extension")
        
        p.path = "."
        self.assertEqual(p.extension, "", "Incorrect extension")
        
        #=======================================================================
        #     Empty extension
        #=======================================================================
        
        p.path = self.basename
        self.assertEqual(p.extension, "", "Incorrect extension")
        
        #=======================================================================
        #     Multiple extension
        #=======================================================================
        
        p.path = "archive.tar.gz"
        self.assertEqual(p.extension, ".gz", "Incorrect extension")
        
        #=======================================================================
        #     Filename
        #=======================================================================
        
        p.path = self.filename
        self.assertEqual(p.extension, self.extension, "Incorrect extension")
        
        #=======================================================================
        #     Local
        #=======================================================================
        
        p.path = self.localFilename
        self.assertEqual(p.extension, self.extension, "Incorrect extension")
        
        #=======================================================================
        #     Local with back
        #=======================================================================
        
        p.path = self.backLocalFilename
        self.assertEqual(p.extension, self.extension, "Incorrect extension")
        
        #=======================================================================
        #     Absolute
        #=======================================================================
        
        p.path = self.absoluteFile
        self.assertEqual(p.extension, self.extension, "Incorrect extension")
        
        #=======================================================================
        #     Absolute Dir
        #=======================================================================
        
        p.path = self.absoluteDirFile
        self.assertEqual(p.extension, self.extension, "Incorrect extension")
        
    def test_parent(self):
        
        p = MyPath()
        p.path = self.localFilename
        parent = p.parent
        self.assertEqual(parent.path, self.localDir, "Incorrect parent")
        
    def test_withFilename(self):
        
        p = MyPath(self.changedFilename)
        
        newP = p.withFilename(self.changedFilename)
        
        self.assertEqual(newP.filename, self.changedFilename, "Incorrect new filename")
        self.assertEqual(newP.path, self.changedFilename, "Incorrect new filename")
        
        p.path = self.localFilename
        newP = p.withFilename(self.changedFilename)
        
        self.assertEqual(newP.filename, self.changedFilename, "Incorrect new filename")
        self.assertEqual(newP.path, self.localChangedFilename, "Incorrect new filename")
        
    def test_withBasename(self):
        
        p = MyPath(self.filename)
        
        newP = p.withBasename(self.otherBasename)
        
        self.assertEqual(newP.basename, self.otherBasename, "Incorrect new basename")
        self.assertEqual(newP.filename, self.changedBasename, "Incorrect new basename")
        self.assertEqual(newP.path, self.changedBasename, "Incorrect new basename")
        
        p.path = self.localFilename
        newP = p.withBasename(self.otherBasename)
        
        self.assertEqual(newP.basename, self.otherBasename, "Incorrect new basename")
        self.assertEqual(newP.filename, self.changedBasename, "Incorrect new basename")
        self.assertEqual(newP.path, self.localChangedBasename, "Incorrect new basename")
        
    def test_withExtension(self):
        
        p = MyPath(self.filename)
        
        newP = p.withExtension(self.otherExtension)
        
        self.assertEqual(newP.extension, self.otherExtension, "Incorrect new extension")
        self.assertEqual(newP.filename, self.changedExtension, "Incorrect new extension")
        self.assertEqual(newP.path, self.changedExtension, "Incorrect new extension")
        
        p.path = self.localFilename
        newP = p.withExtension(self.otherExtension)
        
        self.assertEqual(newP.extension, self.otherExtension, "Incorrect new extension")
        self.assertEqual(newP.filename, self.changedExtension, "Incorrect new extension")
        self.assertEqual(newP.path, self.localChangedExtension, "Incorrect new extension")
    
    
    """def test_createEmpty(self):
        
        p = Path()
        
        self.assertEqual(p.path, ".")
        
        self.assertEqual(p.absolutePath, os.path.abspath(""))
        self.assertEqual(p.filename, "")
        
        self.assertEqual(p.basename, "")
        self.assertEqual(p.absoluteBasename, os.path.abspath(""))
        
        self.assertEqual(p.extension, "")
    
    def test_filename(self):
        
        path = "file.pdf"
        p = Path(path)
        
        self.assertEqual(p.path, "file.pdf")
        
        self.assertEqual(p.absolutePath, os.path.abspath("") + "/file.pdf")
        self.assertEqual(p.filename, "file.pdf")
        
        self.assertEqual(p.basename, "file")
        self.assertEqual(p.absoluteBasename, os.path.abspath("") + "/file")
        
        self.assertEqual(p.extension, ".pdf")
    
    def test_localPath(self):
        
        path = self.localPath
        p = Path(path)
        
        self.assertEqual(p.path, path)
        
        self.assertEqual(p.filename, "file.pdf")
        
        self.assertEqual(p.basename, "file")
        self.assertEqual(p.absoluteBasename, "a/b/cd/file")
        
        self.assertEqual(p.extension, ".pdf")
    
    def test_backLocalPath(self):
        
        path = "a/b/../cd/file.pdf"
        p = Path(path)
        
        self.assertEqual(p.path, path)
        
        self.assertEqual(p.filename, "file.pdf")
        
        self.assertEqual(p.basename, "file")
        self.assertEqual(p.absoluteBasename, "a/b/cd/file")
        
        self.assertEqual(p.extension, ".pdf")
    
    def test_createMultipleExtensions(self):
        path = "a/b/c.tar.gz"
        p = Path(path)
        self.assertEqual(p.getAbsolutePath(), "a/b/c.tar.gz")
        self.assertEqual(p.getAbsoluteBasename(), "a/b/c.tar")
        self.assertEqual(p.getFileName(), "c.tar.gz")
        self.assertEqual(p.getFileBasename(), "c.tar")
        self.assertEqual(p.getExtension(), ".gz")"""

if __name__ == '__main__':
    unittest.main()

