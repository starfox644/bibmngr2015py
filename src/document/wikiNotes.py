# -*- coding: utf-8 -*-

from fs.file import File
from .documentFields import DocumentFields
from .notes import Notes

class WikiNotes(Notes):

    TABLE_HEADER = "{| border=\"0\" cellpadding=\"2\" cellspacing=\"0\"\n"

    TABLE_END = "|}"

    FILENAME = "notes.wiki"

    def __init__(self, fields):
        Notes.__init__(self, fields)

    def getFormattedTitle(self, title):
        return ""

    def getFileName(self):
        return self.FILENAME

    def getHeader(self):
        return ""

    def getDescTableHeader(self):
        return self.TABLE_HEADER

    def getDescTableEnd(self):
        return self.TABLE_END

    def getFieldTableEntry(self, name, value):
        entry = "|" + name + " :\n"
        entry += "| \'\'\'" + value + "\'\'\'\n"
        entry += "|-\n"
        return entry

