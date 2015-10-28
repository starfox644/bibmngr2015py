import sys
sys.path.append("../..")

from tests.test import Test

from document.documentFields import DocumentFields
from document.latexNotes import LatexNotes

class TestLatexNotes(Test):
    def __init__(self):
        Test.__init__(self, "LatexNotes")
        self.addTestFunction(self.emptyContent)
        self.addTestFunction(self.titleContent)

    def emptyContent(self):
        d = DocumentFields()
        notes = LatexNotes(d)
        content = notes.getDocumentContent()
        expectedContent = LatexNotes.HEADER + "\n" + "\\end{document}"
        assert(content == expectedContent)

    def titleContent(self):
        d = DocumentFields()
        d.setField("title", "document about internet")
        notes = LatexNotes(d)
        notes.createTitle()
        content = notes.getDocumentContent()
        expectedContent = LatexNotes.HEADER
        expectedContent += "\n"
        expectedContent += "\\title{document about internet}\n"
        expectedContent += "\\maketitle\n"
        expectedContent += "\n"
        expectedContent += "\\end{document}"
        assert(content == expectedContent)

t = TestLatexNotes()
t.runTests()

