import sys
sys.path.append("../..")

class Test:
    def __init__(self, moduleName):
        self.moduleName = moduleName
        self.tests = []
        
    def addTestFunction(self, f):
        self.tests.append(f)
        
    def runTests(self):
        for function in self.tests:
            function()
        print "Tests for ", self.moduleName, " are ok"


