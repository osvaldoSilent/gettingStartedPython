from .BaseFile import BaseFile
from io import open
class HandlerFile(BaseFile):
    pass
    def __int__(self,path):
        super().__int__(path)
    def read(self):
        f = open(self.getPath(), "r")
        for i in f.readlines():
            print(i)
        f.close()
    def create(self):
        try:
            f = open(self.getPath(), "r")
            print(f"File '{self.getPath()}' already exists")
            f.close()
        except:
            f = open(self.getPath(), "w")
            print(f"File '{self.getPath()}' created")
            f.close()
    def write(self, lines):
        try:
            f = open(self.getPath(), "r")
            f = open(self.getPath(), "a")
            f.seek(0)
            f.write(lines)
        except:
            f = open(self.getPath(), "w")
            print(f"File '{self.getPath()}' created")
        finally:
            f.close()
    def overWrite(self, lines):
        try:
            f = open(self.getPath(), "r")
            f = open(self.getPath(), "w")
            f.write(lines)
        except:
            f = open(self.getPath(), "w")
            print(f"File '{self.getPath()}' created")
        finally:
            f.close()