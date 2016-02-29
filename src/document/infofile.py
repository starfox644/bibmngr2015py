from fs.file import File
import json

class Infofile:
    
    def __init__(self):
        self._title = ""
        
    def getTitle(self):
        return self._title
    
    def setTitle(self, title):
        self._title = title
        
    title = property(getTitle, setTitle)
    
    def readContent(self, path):
        
        success = False
        
        file = File(path)
        jsonContent = file.readContent()
        
        if(jsonContent is not None):
            
            content = json.loads(jsonContent)
            title = content.get("title")
            
            if(title is not None):
                self._title = title
                success = True
                
        return success
    
    def writeContent(self, path):
        
        file = File(path)
        
        content = {'title' : self._title}
        jsonContent = json.dumps(content)
        
        print("Content : ", jsonContent)
        print("Write to : ", path.path)
        
        file.writeContent(jsonContent)