# -*- coding: utf-8 -*-

from difflib import *
import difflib
from document.documentFields import DocumentFields
from document.notes import Notes
import sys
from tests.test import Test


sys.path.append("../..")




class TestNotes(Test):
    def __init__(self):
        Test.__init__(self, "Notes")
        self.addTestFunction(self.emptyContent)
        self.addTestFunction(self.titleContent)
        self.addTestFunction(self.descTableYear)
        self.addTestFunction(self.descTableAuthors)
        self.addTestFunction(self.descTableKeywords)
        self.addTestFunction(self.descTableJournal)
        self.addTestFunction(self.descTableAll)
        self.addTestFunction(self.descAll)

    def emptyContent(self):
        d = DocumentFields()
        notes = Notes(d)
        content = notes.getDocumentContent()
        expectedContent = ""
        # print expectedContent
        assert(content == expectedContent)

    def titleContent(self):
        d = DocumentFields()
        d.setField("title", "document about internet")
        notes = Notes(d)
        notes.createTitle()
        content = notes.getDocumentContent()
        expectedContent = "document about internet\n\n"
        # print content
        # print expectedContent
        assert(content == expectedContent)

    def descTableYear(self):
        d = DocumentFields()
        d.setField("year", "2014")
        notes = Notes(d)
        notes.createDescriptionTable()
        content = notes.getDocumentContent()
        expectedContent = Notes.TABLE_HEADER
        expectedContent += "Annee = 2014\n"
        expectedContent += Notes.TABLE_END
        # contentLines = content.splitlines()
        # expLines = expectedContent.splitlines()
        # d = difflib.Differ()
        # diff = d.compare(contentLines, expLines)
        # print "\n".join(diff)
        assert(content == expectedContent)

    def descTableAuthors(self):
        d = DocumentFields()
        d.setField("author", "Bruf, John and Bamo, Tomy")
        notes = Notes(d)
        notes.createDescriptionTable()
        content = notes.getDocumentContent()
        expectedContent = Notes.TABLE_HEADER
        expectedContent += "Auteurs = John Bruf, Tomy Bamo\n"
        expectedContent += Notes.TABLE_END
        # contentLines = content.splitlines()
        # expLines = expectedContent.splitlines()
        # d = difflib.Differ()
        # diff = d.compare(contentLines, expLines)
        # print ("\n".join(diff))
        assert(content == expectedContent)

    def descTableKeywords(self):
        d = DocumentFields()
        d.setField("keywords", "Computer science, Photography")
        notes = Notes(d)
        notes.createDescriptionTable()
        content = notes.getDocumentContent()
        expectedContent = Notes.TABLE_HEADER
        expectedContent += "Mots-cles = Computer science, Photography\n"
        expectedContent += Notes.TABLE_END
        # contentLines = content.splitlines()
        # expLines = expectedContent.splitlines()
        # d = difflib.Differ()
        # diff = d.compare(contentLines, expLines)
        # print "\n".join(diff)
        assert(content == expectedContent)

    def descTableJournal(self):
        d = DocumentFields()
        d.setField("journal", "Journal of Computer Science")
        notes = Notes(d)
        notes.createDescriptionTable()
        content = notes.getDocumentContent()
        expectedContent = Notes.TABLE_HEADER
        expectedContent += "Journal = Journal of Computer Science\n"
        expectedContent += Notes.TABLE_END
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
        notes = Notes(d)
        notes.createDescriptionTable()
        content = notes.getDocumentContent()
        expectedContent = Notes.TABLE_HEADER
        expectedContent += "Annee = 2014\n"
        expectedContent += "Auteurs = John Bruf, Tomy Bamo\n"
        expectedContent += "Mots-cles = Computer science, Photography\n"
        expectedContent += "Journal = Journal of Computer Science\n"
        expectedContent += Notes.TABLE_END

        # contentLines = content.splitlines()
        # expLines = expectedContent.splitlines()
        # d = difflib.Differ()
        # diff = d.compare(contentLines, expLines)
        # print "\n".join(diff)

        assert(content == expectedContent)

    def descAll(self):
        d = DocumentFields()
        d.setField("title", "document about internet")
        d.setField("year", "2014")
        d.setField("author", "Bruf, John and Bamo, Tomy")
        d.setField("keywords", "Computer science, Photography")
        d.setField("journal", "Journal of Computer Science")
        notes = Notes(d)
        notes.createAllContent()
        content = notes.getDocumentContent()
        expectedContent = "document about internet\n\n"
        expectedContent += Notes.TABLE_HEADER
        expectedContent += "Annee = 2014\n"
        expectedContent += "Auteurs = John Bruf, Tomy Bamo\n"
        expectedContent += "Mots-cles = Computer science, Photography\n"
        expectedContent += "Journal = Journal of Computer Science\n"
        expectedContent += Notes.TABLE_END

        # contentLines = content.splitlines()
        # expLines = expectedContent.splitlines()
        # d = difflib.Differ()
        # diff = d.compare(contentLines, expLines)
        # print ("\n".join(diff))

        assert(content == expectedContent)

t = TestNotes()
t.runTests()

