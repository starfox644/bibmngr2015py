import subprocess
from pathlib import PurePath

class Converter:
    
    LATEX = 0
    MEDIAWIKI = 1
    OTHER = 2
    
    ALL_TYPES_LIST = [LATEX, MEDIAWIKI, OTHER]
    
    LATEX_SUFFIX = ".tex"
    MEDIAWIKI_SUFFIX = ".wiki"
    
    LATEX_TYPE = "latex"
    MEDIAWIKI_TYPE = "mediawiki"
    
    def __init__(self):
        self._inputFile = ""
        self._inputType = None
        self._outputFile = ""
        self._outputType = None
        
    def typeToStr(self, filetype):
        if(filetype == self.LATEX):
            return self.LATEX_TYPE
        elif(filetype == self.MEDIAWIKI):
            return self.MEDIAWIKI_TYPE
        else:
            raise ValueError("Unable to convert the type to a string")
        
    def typeToSuffix(self, filetype):
        if(filetype == self.LATEX):
            return self.LATEX_SUFFIX
        elif(filetype == self.MEDIAWIKI):
            return self.MEDIAWIKI_SUFFIX
        else:
            raise ValueError("Unable to get the suffix of the type")
        
    def guessOutputFile(self, outputType):
        if(not self._inputFile):
            raise ValueError("No input file given")
        
        path = PurePath(self._inputFile)
        parent = path.parent
        name = path.stem
        suffix = self.typeToSuffix(outputType)
        
        outputFile = str(parent) + "/" + name + suffix
        
        return outputFile
        
    def __guessType(self, name):
        path = PurePath(name)
        suffix = path.suffix
        filetype = self.OTHER
        
        if(suffix == self.LATEX_SUFFIX):
            filetype = self.LATEX
            
        elif(suffix == self.MEDIAWIKI_SUFFIX):
            filetype = self.MEDIAWIKI
        
        return filetype
        
    def __checkFileType(self, filetype):
        if(filetype is None):
            raise ValueError("File type must not be None")
        
        if(not filetype in self.ALL_TYPES_LIST):
            raise ValueError("File type unknown, must be defined by the predefined values in class Converter")
        
    @property
    def inputType(self):
        return self._inputType
    
    @property
    def outputType(self):
        return self._outputType
        
    def setInputFile(self, file, filetype=None):
        if(filetype is not None):
            self.__checkFileType(filetype)
            self._inputType = filetype
        else:
            self._inputType = None
            
        self._inputFile = file
            
    def setOutputFile(self, file, filetype=None):
        if(filetype is not None):
            self.__checkFileType(filetype)
            self._outputType = filetype
        else:
            self._outputType = None
            
        self._outputFile = file
    
    def convert(self):
        
        if(not self._inputFile):
            raise ValueError("No input file given")
        
        if(not self._outputFile):
            raise ValueError("No output file given")
        
        if(self._inputType is None):
            self._inputType = self.__guessType(self._inputFile)
            if(self._inputType == self.OTHER):
                print("Unable to get the filetype of input file, conversion aborted")
                
        if(self._outputType is None):
            self._outputType = self.__guessType(self._outputFile)
            if(self._outputType == self.OTHER):
                print("Unable to get the filetype of output file, conversion aborted")
                
        command = ['pandoc']
        
        command.append("-f")
        command.append(self.typeToStr(self._inputType))
        
        command.append("-t")
        command.append(self.typeToStr(self._outputType))
        
        command.append("-s")
        command.append(self._inputFile)
        
        command.append("-o")
        command.append(self._outputFile)
        
        res = subprocess.run(command)
        
        return (res.returncode == 0)
        
    
    
    
    
    
    
    
    
    
    
    
    
    