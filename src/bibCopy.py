#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import argparse
from pathlib import Path
from pathlib import PurePath
import shutil

import sys
sys.path.append(".")

inputPath = ""
outputPath = ""

def printFolder(path):
    print("In folder : ", str(path))

def recursiveGlob(path, fun = None):
    content = path.glob("*")
    
    if(fun is not None):
        fun(path)
    
    for d in content:
        if(d.is_dir()):
            purePath = PurePath(str(path))
            name = purePath.name
            if(not name.startswith(".")):
                recursiveGlob(d, fun)
                
def containsDocuments(path):
    texDocs = list(path.glob("*.tex"))
    wikiDocs = list(path.glob("*.wiki"))
    bibDocs = list(path.glob("*.bib"))
    
    return (texDocs or wikiDocs or bibDocs)   

def copyDocuments(inputPath, outputPath):

    texDocs = list(inputPath.glob("*.tex"))
    wikiDocs = list(inputPath.glob("*.wiki"))
    bibDocs = list(inputPath.glob("*.bib"))
        
    docs = texDocs + wikiDocs + bibDocs 
    
    for d in docs:
        purePath = PurePath(str(d))
        name = purePath.name
        inDoc = str(d)
        outDoc = str(outputPath) + "/" + name
        print("Copy ", inDoc, " to ", outDoc)
        shutil.copyfile(inDoc, outDoc)
                
def recursiveCreate(path):
    purePath = PurePath(str(path))
    
    parts = list(purePath.parts)
    parts = parts[1:]
    
    curr = ""
    
    for p in parts:
        if(str(p).startswith(".")):
            break
        curr += str(p) + "/"
        
        currIn = Path(str(inputPath) + "/" + curr)
        currOut = Path(str(outputPath) + "/" + curr)
        
        if(containsDocuments(currIn)):
            if(not currOut.is_dir()):
                print("Create ", str(currOut))
                currOut.mkdir()
            copyDocuments(currIn, currOut)

def main():
    global inputPath
    global outputPath
    
    parser = argparse.ArgumentParser(description='Crée le dossier d\'un document à partir d\'un fichier bibtex')
    parser.add_argument('input', help='racine du dossier contenant les notes')
    parser.add_argument('output', help="racine du dossier ou les notes doivent etre copiees")
    args = parser.parse_args()
    
    inputPath = Path(args.input)
    outputPath = Path(args.output)
    
    if(not inputPath.is_dir()):
        print("Error : input path is not a directory")
    
    if(not outputPath.is_dir()):
        print("Error : output path is not a directory")
        
    print("Input : ")    
    print("")
    recursiveGlob(inputPath, recursiveCreate)
    print("")
    
if __name__ == '__main__':
    main()
