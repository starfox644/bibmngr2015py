import sys
sys.path.append("../..")

from fs.directory import Directory
from fs.file import File
from fs.path import Path
from tests.test import Test

class TestDirectory(Test):
    def __init__(self):
        Test.__init__(self, "Directory")
        d = Directory("dir")
        d.removeDir()
        self.addTestFunction(self.create)
        self.addTestFunction(self.remove)
        self.addTestFunction(self.createTree)
        self.addTestFunction(self.content)
        self.addTestFunction(self.containsFolder)

    def create(self):
        d = Directory("dir")
        assert(not d.exists())
    
        d.createDir()
        assert(d.exists())
        assert(not d.isRegularFile())
        assert(d.isDirectory())
    
    def remove(self):
        d = Directory("dir")
        d.removeFile()
        assert(d.exists())
    
        d.removeDir()
        assert(not d.exists())
    
    def createTree(self):
        d = Directory("dir/fg/a")
        assert(not d.exists())
    
        d.createDir()
        assert(not d.exists())
    
        d.createTree()
        assert(d.exists())
    
        d.removeFile()
        assert(d.exists())
    
        d.removeDir()
        assert(not d.exists())
    
        d = Directory("dir")
        assert(d.exists())
    
        d.removeDir()
        assert(not d.exists())
        
    def content(self):
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
        assert (l == {"dir/e.txt", "dir/g.txt"})
        
        l = d.getDirsList()
        assert (l == {"dir/a", "dir/c", "dir/d"})
        
        l = d.getContentList()
        assert (l == {"dir/e.txt", "dir/g.txt", "dir/a", "dir/c", "dir/d"})
        
        d.removeDir()

    def containsFolder(self):
        d = Directory("dir")
        d1 = Directory("dir/a/b")
        d2 = Directory("dir/c")
        d3 = Directory("dir/a")

        d1.createTree()
        d2.createTree()

        assert(d.containsFolder("a"))
        assert(d.containsFolder("c"))
        assert(not d.containsFolder("b"))
        assert(d3.containsFolder("b"))
        assert(not d3.containsFolder("a"))

        d.removeDir()


t = TestDirectory()
t.runTests()







