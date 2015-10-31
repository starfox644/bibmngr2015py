# -*- coding: utf-8 -*-

import sys
sys.path.append("../..")

from fs.path import Path
from tests.test import Test
    
class TestPath(Test):
    
    def __init__(self):
        Test.__init__(self, "Path")
        self.addTestFunction(self.createEmpty)
        self.addTestFunction(self.createLocal)
        self.addTestFunction(self.createAbsolute)
        self.addTestFunction(self.createNotClean)
        self.addTestFunction(self.createMultipleExtensions)
    
    def createEmpty(self):
        p = Path()
        assert(p.getAbsolutePath() == "")
        assert(p.getAbsoluteBasename() == "")
        assert(p.getFileName() == "")
        assert(p.getFileBasename() == "")
        assert(p.getExtension() == "")
    
    def createLocal(self):
        path = "file.pdf"
        p = Path(path)
        assert(p.getAbsolutePath() == "file.pdf")
        assert(p.getAbsoluteBasename() == "file")
        assert(p.getFileName() == "file.pdf")
        assert(p.getFileBasename() == "file")
        assert(p.getExtension() == ".pdf")
    
    def createAbsolute(self):
        path = "a/b/cd/file.pdf"
        p = Path(path)
        assert(p.getAbsolutePath() == "a/b/cd/file.pdf")
        assert(p.getAbsoluteBasename() == "a/b/cd/file")
        assert(p.getFileName() == "file.pdf")
        assert(p.getFileBasename() == "file")
        assert(p.getExtension() == ".pdf")
    
    def createNotClean(self):
        path = "a/b/../cd//file.pdf"
        p = Path(path)
        assert(p.getAbsolutePath() == "a/cd/file.pdf")
        assert(p.getAbsoluteBasename() == "a/cd/file")
        assert(p.getFileName() == "file.pdf")
        assert(p.getFileBasename() == "file")
        assert(p.getExtension() == ".pdf")
    
    def createMultipleExtensions(self):
        path = "a/b/c.tar.gz"
        p = Path(path)
        assert(p.getAbsolutePath() == "a/b/c.tar.gz")
        assert(p.getAbsoluteBasename() == "a/b/c.tar")
        assert(p.getFileName() == "c.tar.gz")
        assert(p.getFileBasename() == "c.tar")
        assert(p.getExtension() == ".gz")

t = TestPath()
t.runTests()

