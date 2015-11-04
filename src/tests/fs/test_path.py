# -*- coding: utf-8 -*-

import sys
sys.path.append("../..")

import unittest
from unittest import TestCase

from fs.path import Path
    
class TestPath(TestCase):
    
    def test_createEmpty(self):
        p = Path()
        self.assertEqual(p.getAbsolutePath(), "")
        self.assertEqual(p.getAbsoluteBasename(), "")
        self.assertEqual(p.getFileName(), "")
        self.assertEqual(p.getFileBasename(), "")
        self.assertEqual(p.getExtension(), "")
    
    def test_createLocal(self):
        path = "file.pdf"
        p = Path(path)
        self.assertEqual(p.getAbsolutePath(), "file.pdf")
        self.assertEqual(p.getAbsoluteBasename(), "file")
        self.assertEqual(p.getFileName(), "file.pdf")
        self.assertEqual(p.getFileBasename(), "file")
        self.assertEqual(p.getExtension(), ".pdf")
    
    def test_createAbsolute(self):
        path = "a/b/cd/file.pdf"
        p = Path(path)
        self.assertEqual(p.getAbsolutePath(), "a/b/cd/file.pdf")
        self.assertEqual(p.getAbsoluteBasename(), "a/b/cd/file")
        self.assertEqual(p.getFileName(), "file.pdf")
        self.assertEqual(p.getFileBasename(), "file")
        self.assertEqual(p.getExtension(), ".pdf")
    
    def test_createNotClean(self):
        path = "a/b/../cd//file.pdf"
        p = Path(path)
        self.assertEqual(p.getAbsolutePath(), "a/cd/file.pdf")
        self.assertEqual(p.getAbsoluteBasename(), "a/cd/file")
        self.assertEqual(p.getFileName(), "file.pdf")
        self.assertEqual(p.getFileBasename(), "file")
        self.assertEqual(p.getExtension(), ".pdf")
    
    def test_createMultipleExtensions(self):
        path = "a/b/c.tar.gz"
        p = Path(path)
        self.assertEqual(p.getAbsolutePath(), "a/b/c.tar.gz")
        self.assertEqual(p.getAbsoluteBasename(), "a/b/c.tar")
        self.assertEqual(p.getFileName(), "c.tar.gz")
        self.assertEqual(p.getFileBasename(), "c.tar")
        self.assertEqual(p.getExtension(), ".gz")

if __name__ == '__main__':
    unittest.main()

