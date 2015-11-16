# -*- coding: utf-8 -*-

import sys
sys.path.append("../..")

import os
import unittest
from unittest import TestCase

from fs.file import File

class TestFile(TestCase):

    def setUp(self):
        if(os.path.exists("hello")):
            os.remove("hello")
        if(os.path.exists("test_read_write.txt")):
            os.remove("test_read_write.txt")
        if(os.path.exists("test_read_write2.txt")):
            os.remove("test_read_write2.txt")

    def test_notExist(self):
        f = File("hello")
        self.assertFalse(f.exists())
    
    def test_create(self):
        f = File("hello")
        f.createFile()
        self.assertTrue(f.exists())
        self.assertTrue(f.isRegularFile())
        self.assertFalse(f.isDirectory())
    
    def test_remove(self):
        f = File("hello")
        f.removeFile()
        self.assertFalse(f.exists())

    def test_move(self):
        f = File("hello")
        f.createFile()
        f.moveFile("newdest")

        self.assertTrue(f.exists())
        self.assertEqual(f.getPath().getAbsolutePath(), "newdest")

        oldFile = File("hello")
        self.assertFalse(oldFile.exists())

        f.removeFile()
        self.assertFalse(f.exists())

    def test_readWrite(self):
        f = File("test_read_write.txt")
        content = "Hello\nI am a file"
        f.writeContent(content)
        readContent = f.readContent()
        self.assertEqual(content, readContent)
        f.removeFile()

        f = File("test_read_write2.txt")
        content = "Hello\nI am a file"
        f.writeContent(content)

        content = "This is another content for the file"
        f.writeContent(content)
        readContent = f.readContent()
        self.assertEqual(content, readContent)
        f.removeFile()

if __name__ == '__main__':
    unittest.main()
