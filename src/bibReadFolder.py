#!/usr/bin/python3

import argparse
from document.document import DocumentFolder

import sys
sys.path.append(".")

def main():
    parser = argparse.ArgumentParser(description="Affiche les infos du dossier d'un document")
    parser.add_argument("path", type=str, help="chemin du dossier")
    args = parser.parse_args()

    path = args.path

    docFolder = DocumentFolder(path)
    docFolder.readInfos()

if __name__ == "__main__":
    main()