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
    
t = TestFile()
t.runTests()

