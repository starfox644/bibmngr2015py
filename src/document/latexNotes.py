# -*- coding: utf-8 -*-

from fs.file import File
from documentFields import DocumentFields
from notes import Notes

class LatexNotes(Notes):

    HEADER = (  "\\documentclass[10pt]{article}\n"
                "\\usepackage[utf8]{inputenc}\n"
                "\\usepackage{graphicx}\n"
                "\\usepackage{longtable}\n"
                "\\usepackage{booktabs}\n"
                "\\usepackage[top=1cm, bottom=1cm, left=1cm, right=1cm]{geometry}\n"
                "\n"
                "\\begin{document}\n\n")

    TABLE_HEADER = ("\\begin{longtable}[c]{@{}ll@{}}\n"
                    "\\toprule\\addlinespace\n"
                    "\n")

    TABLE_END = ( "\\bottomrule\n"
            "\\end{longtable}\n\n")

    FILENAME = "notes.tex"

    def __init__(self, fields):
        Notes.__init__(self, fields)

    def getDocumentContent(self):
        content = Notes.getDocumentContent(self)
        return (content + "\end{document}\n")

    def getFormattedTitle(self, title):
        formTitle = "\\title{" + title + "}\n"
        formTitle += "\\maketitle\n\n"
        return formTitle

    def getFileName(self):
        return self.FILENAME

    def getHeader(self):
        return self.HEADER

    def getDescTableHeader(self):
        return self.TABLE_HEADER

    def getDescTableEnd(self):
        return self.TABLE_END

    def getFieldTableEntry(self, name, value):
        entry = name + " : & \\textbf{" + value + "}\n"
        entry += "\\\\\\addlinespace\n\n"
        return entry

