from documentFields import DocumentFields

class LatexNotes:

    HEADER = (  "\\documentclass[10pt]{article}\n"
                "\\usepackage[utf8]{inputenc}\n"
                "\\usepackage{graphicx}\n"
                "\\usepackage{longtable}\n"
                "\\usepackage{booktabs}\n"
                "\\usepackage[top=1cm, bottom=1cm, left=1cm, right=1cm]{geometry}\n"
                "\n"
                "\\begin{document}\n")

    def __init__(self, fields):
        self.fields_ = fields
        self.content = self.HEADER

    def getDocumentContent(self):
        return (self.content + "\n" + "\end{document}")

    def createTitle(self):
        if (self.fields_.hasTitle()):
            self.content += "\n"
            self.content += "\\title{" + self.fields_.getField("title") + "}\n"
            self.content += "\\maketitle"
            self.content += "\n"

    def createDescriptionTable(self):
        None

