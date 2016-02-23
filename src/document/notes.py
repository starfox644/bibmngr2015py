# -*- coding: utf-8 -*-

from fs.file import File

from .fieldsFormatting import *


class Notes:

    TABLE_HEADER = "----- Description -----\n\n"
    TABLE_END = "-----------------------\n\n"

    FIELDS_IN_TABLE = ["year", "author", "journal", "booktitle"]
    TRANSLATION = {'year':'Annee', 'author':"Auteurs", "keyword":"Mots-cles", "booktitle":"revue"}

    def __init__(self, fields):
        self.fields_ = fields
        self.content_ = self.getHeader()

    def getDocumentContent(self):
        content = self.content_ + self.getContentEnd()
        return content

    def getHeader(self):
        return ""

    def getContentEnd(self):
        return ""

    def getFileName(self):
        return "notes.txt"

    def writeContent(self, folderPath):
        f = File(folderPath + "/" + self.getFileName())
        f.writeContent(self.getDocumentContent())

    def getFormattedTitle(self, title):
        return title + "\n\n"

    def createTitle(self):
        if (self.fields_.hasTitle()):
            title = self.fields_.getField("title")
            self.content_ += self.getFormattedTitle(title)

    def getDescTableHeader(self):
        return self.TABLE_HEADER

    def getDescTableEnd(self):
        return self.TABLE_END

    def getFieldTableEntry(self, name, value):
        return name + " = " + value + "\n"

    def formatField(self, fieldName, fieldValue):
        newFieldValue = fieldValue
        if(fieldName == "author"):
            newFieldValue = formatAuthors(fieldValue)
        elif(fieldName == "journal"):
            newFieldValue = formatJournal(fieldValue)
        return newFieldValue

    def addFieldInTable(self, tableContent, fieldName):
        content = tableContent
        if (self.fields_.hasField(fieldName)):
            fieldValue = self.fields_.getField(fieldName)
            fieldValue = self.formatField(fieldName, fieldValue)
            if (fieldName in self.TRANSLATION):
                name = self.TRANSLATION[fieldName]
            else:
                name = fieldName.title()
            content += self.getFieldTableEntry(name, fieldValue)
        return content

    def createDescriptionTable(self):
        descTable = self.getDescTableHeader()

        for fieldName in self.FIELDS_IN_TABLE:
            descTable = self.addFieldInTable(descTable, fieldName)

        descTable += self.getDescTableEnd()
        self.content_ += descTable

    def createAllContent(self):
        self.createTitle()
        self.createDescriptionTable()

