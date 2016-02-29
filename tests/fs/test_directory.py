#! /usr/bin/python3.5

import sys
sys.path.append("../../src")

from fs.directory import Directory
from fs.file import File
from fs.myPath import MyPath
import os
import shutil
from unittest import TestCase
import unittest

sys.path.append("../..")

class TestDirectory(TestCase):

    def setUp(self):
        if(os.path.exists("dir")):
            shutil.rmtree("dir")

    def test_create(self):
        d = Directory("dir")
        self.assertFalse(d.exists())
    
        d.createDir()
        self.assertTrue(d.exists())
        self.assertFalse(d.isRegularFile())
        self.assertTrue(d.isDirectory())
    
    def test_remove(self):
        d = Directory("dir")
        d.createDir()
        
        d.removeFile()
        self.assertTrue(d.exists())
    
        d.removeDir()
        self.assertFalse(d.exists())
    
    def test_createTree(self):
        d = Directory("dir/fg/a")
        self.assertFalse(d.exists())
    
        with self.assertRaises(FileNotFoundError):
            d.createDir()
            
        self.assertFalse(d.exists())
    
        d.createTree()
        self.assertTrue(d.exists())
    
        d.removeFile()
        self.assertTrue(d.exists())
    
        d.removeDir()
        self.assertFalse(d.exists())
    
        d = Directory("dir")
        self.assertTrue(d.exists())
    
        d.removeDir()
        self.assertFalse(d.exists())
        
    def test_content(self):
        d = Directory("dir")
        d1 = Directory("dir/a/b")
        d2 = Directory("dir/c")
        d3 = Directory("dir/d/e")
        f1 = File("dir/g.txt")
        f2 = File("dir/e.txt")
        
        d1.createTree()
        d2.createTree()
        d3.createTree()
        f1.createFile()
        f2.createFile()
        
        l = d.getFilesList()
        self.assertEqual(l,  {"dir/e.txt", "dir/g.txt"})
        
        l = d.getDirsList()
        self.assertEqual(l, {"dir/a", "dir/c", "dir/d"})
        
        l = d.getContentList()
        self.assertEqual(l, {"dir/e.txt", "dir/g.txt", "dir/a", "dir/c", "dir/d"})
        
        d.removeDir()

    def test_containsFolder(self):
        d = Directory("dir")
        d1 = Directory("dir/a/b")
        d2 = Directory("dir/c")
        d3 = Directory("dir/a")

        d1.createTree()
        d2.createTree()

        self.assertTrue(d.containsFolder("a"))
        self.assertTrue(d.containsFolder("c"))
        self.assertFalse(d.containsFolder("b"))
        self.assertTrue(d3.containsFolder("b"))
        self.assertFalse(d3.containsFolder("a"))

        d.removeDir()
        
    def test_containsExtension(self):
        d = Directory("dir")
        f1 = File("dir/text.txt")
        f2 = File("dir/image.png")
        
        d.createDir()
        
        f1.createFile()
        f2.createFile()
        
        self.assertTrue(d.containsFileExtension(".txt"), "Directory contains .txt")
        self.assertTrue(d.containsFileExtension(".png"), "Directory contains .png")
        self.assertFalse(d.containsFileExtension(".pdf"), "Directory does not contain .pdf")
        
        d.removeDir()

if __name__ == '__main__':
    unittest.main()







