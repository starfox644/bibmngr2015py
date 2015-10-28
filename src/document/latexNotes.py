# -*- coding: utf-8 -*-

from fs.file import File
from documentFields import DocumentFields

class LatexNotes:

    # TODO : translation table for fields names

    HEADER = (  "\\documentclass[10pt]{article}\n"
                "\\usepackage[utf8]{inputenc}\n"
                "\\usepackage{graphicx}\n"
                "\\usepackage{longtable}\n"
                "\\usepackage{booktabs}\n"
                "\\usepackage[top=1cm, bottom=1cm, left=1cm, right=1cm]{geometry}\n"
                "\n"
                "\\begin{document}\n\n")

    FIELDS_IN_TABLE = ["year", "authors", "keywords", "journal"]
    TRANSLATION = {'year':'Année', 'authors':"Auteurs", "keywords":"Mots-clés"}

    FILENAME = "notes.tex"

    def __init__(self, fields):
        self.fields_ = fields
        self.content = self.HEADER

    def getDocumentContent(self):
        return (self.content + "\end{document}\n")

    def writeContent(self, folderPath):
        f = File(folderPath + "/" + self.FILENAME)
        f.writeContent(self.getDocumentContent())

    def createTitle(self):
        if (self.fields_.hasTitle()):
            self.content += "\\title{" + self.fields_.getField("title") + "}\n"
            self.content += "\\maketitle\n\n"

    def addFieldInTable(self, tableContent, fieldName):
        content = tableContent
        if (self.fields_.hasField(fieldName)):
            fieldValue = self.fields_.getField(fieldName)
            if (fieldName in self.TRANSLATION):
                name = self.TRANSLATION[fieldName]
            else:
                name = fieldName.title()
            content += name + " : & \\textbf{" + fieldValue + "}\n"
            content += "\\\\\\addlinespace\n\n"
        return content

    def createDescriptionTable(self):
        descTable = "\\begin{longtable}[c]{@{}ll@{}}\n"
        descTable += "\\toprule\\addlinespace\n\n"

        for fieldName in self.FIELDS_IN_TABLE:
            descTable = self.addFieldInTable(descTable, fieldName)

        descTable += "\\bottomrule\n"
        descTable += "\\end{longtable}\n\n"
        self.content += descTable

    def createAllContent(self):
        self.createTitle()
        self.createDescriptionTable()

