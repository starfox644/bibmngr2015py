#!/usr/bin/python3

import argparse
from document.document import Document

import sys
sys.path.append(".")

def main():
    parser = argparse.ArgumentParser(description='Crée le dossier d\'un document à partir d\'un fichier bibtex')
    parser.add_argument('bib', help='le fichier bibtex du document')
    parser.add_argument("-", "--path", type=str, help="chemin du dossier où créer le dossier du document")
    args = parser.parse_args()

    bibfile = args.bib
    path = args.path

    doc = Document()
    if(doc.readFields(bibfile)):
        doc.createDocumentFolder(bibfile, path)

if __name__ == "__main__":
    main()