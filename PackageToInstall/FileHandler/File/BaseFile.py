class BaseFile:
    pass
    def __int__(self, path):
        self.__path = path
    def setPath(self, path):
        self.__path= path
    def getPath(self):
        return self.__path
