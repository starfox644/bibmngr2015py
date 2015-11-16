#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("../")

import argparse
from bibtex.bibtexReader import BibtexReader

def main():
    parser = argparse.ArgumentParser(description='Affiche le contenu d\'un fichier bibtex')
    parser.add_argument('file', help='le fichier bibtex du document')
    args = parser.parse_args()

    bibfile = args.file

    bibReader = BibtexReader(bibfile)
    fields = bibReader.read()
    if(fields != None):
        print(fields)

if __name__ == "__main__":
    main()