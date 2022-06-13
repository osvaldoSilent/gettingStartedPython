from .base.FileBase import FileBase
from .reader_writer.FileWritterReader import Reader_Writter

class MainHandler:
    pass
    def __init__(self):
        pass
    def operationR(self, operation, path, extension, encoding):
        f = FileBase(path,extension)
        if( str(operation).lower() == "read"):
            self.read(f,encoding)
    def operationW(self, operation, path, extension, encoding, lines):
        lines = str(lines).split("//line//")
        f = FileBase(path,extension)
        if( str(operation).lower() == "write" ):
            self.write(f,encoding, lines)
            pass
        elif( str(operation).lower() == "write_from_zero" ):
            pass

    def getFormat(self, extension):
        if(extension == ".txt"):
            return "r"
        else:
            pass

    def read(self,f, encoding):
        reader = Reader_Writter(f)
        reader.read(self.getFormat(f.extension), encoding)
        pass

    def write(self,f, encoding, lines):
        reader = Reader_Writter(f)
        reader.write(encoding, lines)
        pass

    def write_from_zero(self,f, encoding,lines):
        reader = Reader_Writter(f)
        reader.write(encoding,lines)
        pass

    def new(self):
        pass

