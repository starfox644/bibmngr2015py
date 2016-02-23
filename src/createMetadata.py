#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import sys

from metadata.metadataFile import SaveFile


sys.path.append("../")


def main():
    parser = argparse.ArgumentParser(description='Crée un fichier de metadonnées sur documents vide')
    parser.add_argument("path", help="chemin fichier à créer")
    args = parser.parse_args()

    path = args.path

    file = SaveFile()
    file.createFile(path)

if __name__ == "__main__":
    main()