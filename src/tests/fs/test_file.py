import sys
sys.path.append("../..")

from tests.test import Test
from fs.file import File

class TestFile(Test):
    def __init__(self):
        Test.__init__(self, "File")
        self.addTestFunction(self.notExist)
        self.addTestFunction(self.create)
        self.addTestFunction(self.remove)
        self.addTestFunction(self.readWrite)
     
    def notExist(self): 
        f = File("hello")
        assert(not f.exists())
    
    def create(self): 
        f = File("hello")
        f.createFile()
        assert(f.exists())
        assert(f.isRegularFile())
        assert(not f.isDirectory())
    
    def remove(self): 
        f = File("hello")
        f.removeFile()
        assert(not f.exists())

    def readWrite(self):
        f = File("test_read_write.txt")
        content = "Hello\nI am a file"
        f.writeContent(content)
        readContent = f.readContent()
        assert(content == readContent)
        f.removeFile()

        f = File("test_read_write2.txt")
        content = "Hello\nI am a file"
        f.writeContent(content)

        content = "This is another content for the file"
        f.writeContent(content)
        readContent = f.readContent()
        assert(content == readContent)
        f.removeFile()
    
t = TestFile()
t.runTests()

