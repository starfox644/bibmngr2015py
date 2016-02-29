#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import argparse
from document.converter import Converter

import sys
sys.path.append(".")

def main():
    parser = argparse.ArgumentParser(description='Crée le dossier d\'un document à partir d\'un fichier bibtex')
    parser.add_argument('input', help='le fichier du document à convertir')
    parser.add_argument("-o", "--output", type=str, help="chemin du fichier de notes de sortie")
    args = parser.parse_args()

    converter = Converter()
    
    try:

        converter.setInputFile(args.input)
        
        outputFile = args.output
        if(outputFile):
            converter.setOutputFile(args.output)
        else:
            outputFile = converter.guessOutputFile(converter.MEDIAWIKI)
            print("Output file : ", outputFile)
            
        converter.setOutputFile(outputFile)
        
    except ValueError as e:
        print("Unable to convert : ", e)
        exit()
        
    success = converter.convert()
    
    if(success):
        print("Conversion successful")
    else:
        print("Error in conversion")

if __name__ == "__main__":
    main()