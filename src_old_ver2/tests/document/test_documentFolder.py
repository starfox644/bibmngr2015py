# -*- coding: utf-8 -*-

import sys
sys.path.append("../..")

from tests.test import Test

from fs.directory import Directory
from fs.file import File
from document.documentFields import DocumentFields
from document.documentFolder import DocumentFolder

class TestDocumentFolder(Test):
    def __init__(self):
        Test.__init__(self, "DocumentFolder")
        self.titles = ["document about  science",
                       "document: about \"science\"",
                       "document: about the \"science\" and the (internet)"]
        self.folderNames = ["document_about_science",
                            "document_about_science",
                            "document_about_science_internet"]
        self.addTestFunction(self.folderName)
        self.addTestFunction(self.create)
        self.addTestFunction(self.internFolders)
        self.addTestFunction(self.organize)

    def folderName(self):
        a = DocumentFields()
        a.setField("title", "document")
        
        d = DocumentFolder()
        d.setDocFields(a)

        for i, title in enumerate(self.titles):
            a.setField("title", title)
            name = d.computeFolderName()
            assert(name == self.folderNames[i])

    def create(self):
        a = DocumentFields()
        a.setField("title", "document")

        d = DocumentFolder()
        d.setDocFields(a)

        for title in self.titles:
            a.setField("title", title)
            d.create()
            assert(d.getDir().exists())
            d.delete()
            assert(not d.getDir().exists())

        dir = Directory("documents")
        dir.createDir()

        for title in self.titles:
            a.setField("title", title)
            d.create(dir.getPath().getAbsolutePath())
            assert(d.getDir().exists())
            d.delete()
            assert(not d.getDir().exists())

        dir.removeDir()

    def internFolders(self):
        a = DocumentFields()
        a.setField("title", "document")

        d = DocumentFolder()
        d.setDocFields(a)
        d.create()

        assert(d.getDir().exists())

        assert(not d.hasVideoFolder())
        assert(not d.hasImageFolder())
        assert(not d.hasNotesFolder())
        assert(not d.hasDescFolder())

        d.createVideoFolder()
        d.createImageFolder()
        d.createNotesFolder()
        d.createDescFolder()

        assert(d.hasVideoFolder())
        assert(d.hasImageFolder())
        assert(d.hasNotesFolder())
        assert(d.hasDescFolder())

        d.delete()

    def organize(self):
        fields = DocumentFields()
        fields.setField("title", "document about internet")
        fields.setField("year", "2014")
        fields.setField("authors", "John Bruf, Tommy Bamo")
        fields.setField("keywords", "Computer science, Photography")
        fields.setField("journal", "Journal of Computer Science")

        dir = Directory("document_about_internet")
        dir.removeDir()

        d = DocumentFolder()
        d.setDocFields(fields)

        d.create()

        assert(not d.hasVideoFolder())
        assert(not d.hasImageFolder())
        assert(not d.hasNotesFolder())
        assert(not d.hasDescFolder())

        d.organize()

        assert(d.hasVideoFolder())
        assert(d.hasImageFolder())
        assert(d.hasNotesFolder())
        assert(d.hasDescFolder())

        notesPath = d.getNotesFilePath()
        print notesPath
        assert(File(notesPath).exists())

        d.delete()


t = TestDocumentFolder()
t.runTests()


