
from io import open
class Reader_Writter:
    pass
    def __init__(self, fileBase):
        self.fileBase = fileBase
        pass
    def read(self, format, encoding):
        f = open((self.fileBase.path+self.fileBase.extension), format, encoding=encoding)
        for i in f.readlines():
            print(i)
        f.close()

    def write(self, encoding, lines):
        f = open((self.fileBase.path+self.fileBase.extension), "a", encoding=encoding)
        for i in lines:
            f.write(i)
        f.close()