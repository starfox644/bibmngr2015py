# -*- coding: utf-8 -*-

from difflib import *
import difflib
from document.documentFields import DocumentFields
from document.latexNotes import LatexNotes
import sys
from tests.test import Test


sys.path.append("../..")




class TestLatexNotes(Test):
    def __init__(self):
        Test.__init__(self, "LatexNotes")
        self.addTestFunction(self.emptyContent)
        self.addTestFunction(self.titleContent)
        self.addTestFunction(self.descTableYear)
        self.addTestFunction(self.descTableAuthors)
        self.addTestFunction(self.descTableKeywords)
        self.addTestFunction(self.descTableJournal)
        self.addTestFunction(self.descTableAll)

    def emptyContent(self):
        d = DocumentFields()
        notes = LatexNotes(d)
        content = notes.getDocumentContent()
        expectedContent = LatexNotes.HEADER + "\\end{document}\n"
        # print expectedContent
        assert(content == expectedContent)

    def titleContent(self):
        d = DocumentFields()
        d.setField("title", "document about internet")
        notes = LatexNotes(d)
        notes.createTitle()
        content = notes.getDocumentContent()
        expectedContent = LatexNotes.HEADER
        expectedContent += "\\title{document about internet}\n"
        expectedContent += "\\maketitle\n"
        expectedContent += "\n"
        expectedContent += "\\end{document}\n"
        # print content
        # print expectedContent
        assert(content == expectedContent)

    def descTableYear(self):
        d = DocumentFields()
        d.setField("year", "2014")
        notes = LatexNotes(d)
        notes.createDescriptionTable()
        content = notes.getDocumentContent()
        expectedContent = LatexNotes.HEADER
        expectedContent += ("\\begin{longtable}[c]{@{}ll@{}}\n"
                            "\\toprule\\addlinespace\n"
                            "\n"
                            "Annee : & \\textbf{2014}\n"
                            "\\\\\\addlinespace\n"
                            "\n"
                            "\\bottomrule\n"
                            "\\end{longtable}\n")
        expectedContent += "\n"
        expectedContent += "\\end{document}\n"
        # contentLines = content.splitlines()
        # expLines = expectedContent.splitlines()
        # d = difflib.Differ()
        # diff = d.compare(contentLines, expLines)
        # print "\n".join(diff)
        assert(content == expectedContent)

    def descTableAuthors(self):
        d = DocumentFields()
        d.setField("author", "Bruf, John and Bamo, Tomy")
        notes = LatexNotes(d)
        notes.createDescriptionTable()
        content = notes.getDocumentContent()
        expectedContent = LatexNotes.HEADER
        expectedContent += ("\\begin{longtable}[c]{@{}ll@{}}\n"
                            "\\toprule\\addlinespace\n"
                            "\n"
                            "Auteurs : & \\textbf{John Bruf, Tomy Bamo}\n"
                            "\\\\\\addlinespace\n"
                            "\n"
                            "\\bottomrule\n"
                            "\\end{longtable}\n")
        expectedContent += "\n"
        expectedContent += "\\end{document}\n"
        # contentLines = content.splitlines()
        # expLines = expectedContent.splitlines()
        # d = difflib.Differ()
        # diff = d.compare(contentLines, expLines)
        # print "\n".join(diff)
        assert(content == expectedContent)

    def descTableKeywords(self):
        d = DocumentFields()
        d.setField("keywords", "Computer science, Photography")
        notes = LatexNotes(d)
        notes.createDescriptionTable()
        content = notes.getDocumentContent()
        expectedContent = LatexNotes.HEADER
        expectedContent += ("\\begin{longtable}[c]{@{}ll@{}}\n"
                            "\\toprule\\addlinespace\n"
                            "\n"
                            "Mots-cles : & \\textbf{Computer science, Photography}\n"
                            "\\\\\\addlinespace\n"
                            "\n"
                            "\\bottomrule\n"
                            "\\end{longtable}\n")
        expectedContent += "\n"
        expectedContent += "\\end{document}\n"
        # contentLines = content.splitlines()
        # expLines = expectedContent.splitlines()
        # d = difflib.Differ()
        # diff = d.compare(contentLines, expLines)
        # print "\n".join(diff)
        assert(content == expectedContent)

    def descTableJournal(self):
        d = DocumentFields()
        d.setField("journal", "Journal of Computer Science")
        notes = LatexNotes(d)
        notes.createDescriptionTable()
        content = notes.getDocumentContent()
        expectedContent = LatexNotes.HEADER
        expectedContent += ("\\begin{longtable}[c]{@{}ll@{}}\n"
                            "\\toprule\\addlinespace\n"
                            "\n"
                            "Journal : & \\textbf{Journal of Computer Science}\n"
                            "\\\\\\addlinespace\n"
                            "\n"
                            "\\bottomrule\n"
                            "\\end{longtable}\n")
        expectedContent += "\n"
        expectedContent += "\\end{document}\n"
        # contentLines = content.splitlines()
        # expLines = expectedContent.splitlines()
        # d = difflib.Differ()
        # diff = d.compare(contentLines, expLines)
        # print "\n".join(diff)
        assert(content == expectedContent)

    def descTableAll(self):
        d = DocumentFields()
        d.setField("title", "document about internet")
        d.setField("year", "2014")
        d.setField("author", "Bruf, John and Bamo, Tomy")
        d.setField("keywords", "Computer science, Photography")
        d.setField("journal", "Journal of Computer Science")
        notes = LatexNotes(d)
        notes.createTitle()
        notes.createDescriptionTable()
        content = notes.getDocumentContent()
        expectedContent = LatexNotes.HEADER
        expectedContent += "\\title{document about internet}\n"
        expectedContent += "\\maketitle\n"
        expectedContent += "\n"
        expectedContent += ("\\begin{longtable}[c]{@{}ll@{}}\n"
                            "\\toprule\\addlinespace\n"
                            "\n"
                            "Annee : & \\textbf{2014}\n"
                            "\\\\\\addlinespace\n"
                            "\n"
                            "Auteurs : & \\textbf{John Bruf, Tomy Bamo}\n"
                            "\\\\\\addlinespace\n"
                            "\n"
                            "Mots-cles : & \\textbf{Computer science, Photography}\n"
                            "\\\\\\addlinespace\n"
                            "\n"
                            "Journal : & \\textbf{Journal of Computer Science}\n"
                            "\\\\\\addlinespace\n"
                            "\n"
                            "\\bottomrule\n"
                            "\\end{longtable}\n")
        expectedContent += "\n"
        expectedContent += "\\end{document}\n"
        # contentLines = content.splitlines()
        # expLines = expectedContent.splitlines()
        # d = difflib.Differ()
        # diff = d.compare(contentLines, expLines)
        # print "\n".join(diff)
        assert(content == expectedContent)

t = TestLatexNotes()
t.runTests()

