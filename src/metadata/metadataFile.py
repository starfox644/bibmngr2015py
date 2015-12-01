from fs.path import Path
from fs.file import File
from lxml import etree

def createDocumentEntry(self, fields):
    None

class SaveFile:

    VERSION = 0.1

    def __init__(self, path=""):
        self.path = Path(path)

    def createFile(self, path):
        self.path = path
        tree = etree.Element("documents")
        file = File(path)
        content = etree.tostring(tree, xml_declaration=True, pretty_print=True, encoding="utf-8")
        print(content.decode("utf-8"))
        file.createFile()
        file.writeContent(content.decode("utf-8"))

    def addDocumentEntry(self, docFields):
        None


