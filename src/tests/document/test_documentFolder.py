# -*- coding: utf-8 -*-

import sys
sys.path.append("../..")

import unittest
from unittest import TestCase

from fs.directory import Directory
from fs.file import File
from document.documentFields import DocumentFields
from document.documentFolder import DocumentFolder

class TestDocumentFolder(TestCase):

    titles = [  "document about  science",
                "document: about \"science\"",
                "document: about the \"science\" and the (internet)",
                "Document About  Science",
                "Document: about \"Science\"",
                "Document: about the \"Science\" and the (Internet)"]
    folderNames = [ "document_about_science",
                    "document_about_science",
                    "document_about_science_internet",
                    "document_about_science",
                    "document_about_science",
                    "document_about_science_internet"]

    def test_folderName(self):
        a = DocumentFields()
        a.setField("title", "document")
        
        d = DocumentFolder()
        d.setDocFields(a)

        for i, title in enumerate(self.titles):
            a.setField("title", title)
            name = d.computeFolderName()
            self.assertEqual(name, self.folderNames[i])

    def test_create(self):
        a = DocumentFields()
        a.setField("title", "document")

        d = DocumentFolder()
        d.setDocFields(a)

        # Creation in local folder
        for title in self.titles:
            a.setField("title", title)
            d.create()
            self.assertTrue(d.getDir().exists())
            d.delete()
            self.assertFalse(d.getDir().exists())

        dir = Directory("documents")
        dir.createDir()

        # Creaton in another folder
        for title in self.titles:
            a.setField("title", title)
            d.create(dir.getPath().getAbsolutePath())
            self.assertTrue(d.getDir().exists())
            d.delete()
            self.assertFalse(d.getDir().exists())

        dir.removeDir()

    def test_internFolders(self):
        a = DocumentFields()
        a.setField("title", "document")

        d = DocumentFolder()
        d.setDocFields(a)
        d.create()

        self.assertTrue(d.getDir().exists())

        self.assertFalse(d.hasVideoFolder())
        self.assertFalse(d.hasImageFolder())
        self.assertFalse(d.hasNotesFolder())
        self.assertFalse(d.hasDescFolder())

        d.createVideoFolder()
        d.createImageFolder()
        d.createNotesFolder()
        d.createDescFolder()

        self.assertTrue(d.hasVideoFolder())
        self.assertTrue(d.hasImageFolder())
        self.assertTrue(d.hasNotesFolder())
        self.assertTrue(d.hasDescFolder())

        d.delete()

    def test_organize(self):
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

        self.assertFalse(d.hasVideoFolder())
        self.assertFalse(d.hasImageFolder())
        self.assertFalse(d.hasNotesFolder())
        self.assertFalse(d.hasDescFolder())

        d.organize()

        self.assertFalse(d.hasVideoFolder())
        self.assertFalse(d.hasImageFolder())
        self.assertFalse(d.hasNotesFolder())
        self.assertFalse(d.hasDescFolder())

        notesPath = d.getNotesFilePath()
        print(notesPath)
        self.assertTrue(File(notesPath).exists())

        d.delete()

    def test_organizeWithFiles(self):
        fields = DocumentFields()
        fields.setField("title", "document about internet")
        d = DocumentFolder()
        d.setDocFields(fields)

        bibfile = File("bibfile.bib")
        bibfile.createFile()
        pdffilename = "pdffile.pdf"
        pdffile = File(pdffilename)
        pdffile.createFile()
        fileList = [bibfile, pdffilename]

        d.create()

        d.organize(fileList)
        self.assertFalse(File("bibfile.bib").exists())
        self.assertFalse(File("pdffile.pdf").exists())

        folderPath = d.getDir().getPath().getAbsolutePath()
        newbibfile = File(folderPath + "/" + "bibfile.bib")
        newpdffile = File(folderPath + "/" + "pdffile.pdf")

        self.assertTrue(newbibfile.exists())
        self.assertTrue(newpdffile.exists())

        d.delete()


if __name__ == '__main__':
    unittest.main()


