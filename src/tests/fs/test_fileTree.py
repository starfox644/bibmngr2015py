# -*- coding: utf-8 -*-

from fs.fileTree import FileTree
import os
import shutil
import sys


sys.path.append("../..")



def printFile(path):
    print(path)

def main():
    if (len(sys.argv) > 1):
        tree = FileTree(sys.argv[0])
        tree.walkDirs(printFile)
        tree.walkFiles(printFile)
        tree.walkDirsAndFiles(printFile)
    print("tests for FileTree are ok")

if __name__ == "__main__":
    main()

