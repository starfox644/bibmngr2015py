# -*- coding: utf-8 -*-

from fs.file import File
from .notes import Notes


class LatexNotes(Notes):

    HEADER = (  "\\documentclass[10pt]{article}\n"
                "\\usepackage[utf8]{inputenc}\n"
                "\\usepackage{graphicx}\n"
                "\\usepackage{booktabs}\n"
                "\\usepackage[top=2cm, bottom=2cm, left=2cm, right=2cm]{geometry}\n"
                "\n"
                "\\begin{document}\n\n")

    END = "\end{document}\n"

    TABLE_HEADER = ("\\begin{tabular}{| l l |}\n"
                    "\\hline \n"
                    "\n")

    TABLE_END = ( "\\hline\n"
            "\\end{tabular}\n\n")

    FILENAME = "notes.tex"

    def __init__(self, fields):
        Notes.__init__(self, fields)

    def getFormattedTitle(self, title):
        formTitle = "\\title{" + title + "}\n"
        formTitle += "\\maketitle\n\n"
        return formTitle

    def getFileName(self):
        return self.FILENAME

    def getHeader(self):
        return self.HEADER

    def getContentEnd(self):
        return self.END

    def getDescTableHeader(self):
        return self.TABLE_HEADER

    def getDescTableEnd(self):
        return self.TABLE_END

    def getFieldTableEntry(self, name, value):
        entry = "& \\\\ \n"
        entry += name + " : & \\textbf{" + value + "} \\\\" + "\n"
        entry += "& \\\\ \n"
        return entry

