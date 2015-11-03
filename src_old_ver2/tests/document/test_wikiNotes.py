# -*- coding: utf-8 -*-

import sys
sys.path.append("../..")

import difflib
from difflib import *

from tests.test import Test

from document.documentFields import DocumentFields
from document.wikiNotes import WikiNotes

class TestWikiNotes(Test):
    def __init__(self):
        Test.__init__(self, "WikiNotes")
        self.addTestFunction(self.emptyContent)
        self.addTestFunction(self.titleContent)
        self.addTestFunction(self.descTableYear)
        self.addTestFunction(self.descTableAuthors)
        self.addTestFunction(self.descTableKeywords)
        self.addTestFunction(self.descTableJournal)
        self.addTestFunction(self.descTableAll)

    def emptyContent(self):
        d = DocumentFields()
        notes = WikiNotes(d)
        content = notes.getDocumentContent()
        expectedContent = ""
        # print expectedContent
        assert(content == expectedContent)

    def titleContent(self):
        d = DocumentFields()
        d.setField("title", "document about internet")
        notes = WikiNotes(d)
        notes.createTitle()
        content = notes.getDocumentContent()
        expectedContent = ""
        # print content
        # print expectedContent
        assert(content == expectedContent)

    def descTableYear(self):
        d = DocumentFields()
        d.setField("year", "2014")
        notes = WikiNotes(d)
        notes.createDescriptionTable()
        content = notes.getDocumentContent()

        expectedContent = WikiNotes.TABLE_HEADER
        expectedContent += ("|Annee :\n"
                            "| \'\'\'2014\'\'\'\n"
                            "|-\n")
        expectedContent += WikiNotes.TABLE_END

        # contentLines = content.splitlines()
        # expLines = expectedContent.splitlines()
        # d = difflib.Differ()
        # diff = d.compare(contentLines, expLines)
        # print "\n".join(diff)
        assert(content == expectedContent)

    def descTableAuthors(self):
        d = DocumentFields()
        d.setField("author", "John Bruf, Tommy Bamo")
        notes = WikiNotes(d)
        notes.createDescriptionTable()
        content = notes.getDocumentContent()

        expectedContent = WikiNotes.TABLE_HEADER
        expectedContent += ( "|Auteurs :\n"
                            "| \'\'\'John Bruf, Tommy Bamo\'\'\'\n"
                            "|-\n")
        expectedContent += WikiNotes.TABLE_END

        contentLines = content.splitlines()
        expLines = expectedContent.splitlines()
        d = difflib.Differ()
        diff = d.compare(contentLines, expLines)
        # print "\n".join(diff)
        assert(content == expectedContent)

    def descTableKeywords(self):
        d = DocumentFields()
        d.setField("keywords", "Computer science, Photography")
        notes = WikiNotes(d)
        notes.createDescriptionTable()
        content = notes.getDocumentContent()

        expectedContent = WikiNotes.TABLE_HEADER
        expectedContent += ("|Mots-cles :\n"
                            "| \'\'\'Computer science, Photography\'\'\'\n"
                            "|-\n")
        expectedContent += WikiNotes.TABLE_END

        # contentLines = content.splitlines()
        # expLines = expectedContent.splitlines()
        # d = difflib.Differ()
        # diff = d.compare(contentLines, expLines)
        # print "\n".join(diff)
        assert(content == expectedContent)

    def descTableJournal(self):
        d = DocumentFields()
        d.setField("journal", "Journal of Computer Science")
        notes = WikiNotes(d)
        notes.createDescriptionTable()
        content = notes.getDocumentContent()

        expectedContent = WikiNotes.TABLE_HEADER
        expectedContent += ("|Journal :\n"
                            "| \'\'\'Journal of Computer Science\'\'\'\n"
                            "|-\n")
        expectedContent += WikiNotes.TABLE_END

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
        d.setField("author", "John Bruf, Tommy Bamo")
        d.setField("keywords", "Computer science, Photography")
        d.setField("journal", "Journal of Computer Science")
        notes = WikiNotes(d)
        notes.createTitle()
        notes.createDescriptionTable()
        content = notes.getDocumentContent()

        expectedContent = WikiNotes.TABLE_HEADER
        expectedContent += ("|Annee :\n"
                            "| \'\'\'2014\'\'\'\n"
                            "|-\n"
                            "|Auteurs :\n"
                            "| \'\'\'John Bruf, Tommy Bamo\'\'\'\n"
                            "|-\n"
                            "|Mots-cles :\n"
                            "| \'\'\'Computer science, Photography\'\'\'\n"
                            "|-\n"
                            "|Journal :\n"
                            "| \'\'\'Journal of Computer Science\'\'\'\n"
                            "|-\n")
        expectedContent += WikiNotes.TABLE_END

        # contentLines = content.splitlines()
        # expLines = expectedContent.splitlines()
        # d = difflib.Differ()
        # diff = d.compare(contentLines, expLines)
        # print "\n".join(diff)
        assert(content == expectedContent)

t = TestWikiNotes()
t.runTests()

