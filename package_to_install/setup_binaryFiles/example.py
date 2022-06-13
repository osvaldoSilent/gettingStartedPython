import pickle
from typing import List, Any


class Persona:
    pass
    def __int__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        pass
    def __str__(self):
        return f"{self.name} { self.age} { self.sex}"

class BinaryFile:
    def __int__(self,fileName):
        self.fileName = fileName
        self.list = []
        try:
            f = open(self.fileName,"rb+")
            self.list=pickle.load(f)
        except:
            pass
    def create(self):
        f = open(self.fileName,"rb+")
        try:
            self.list=pickle.load(f)
            print(f"{self.fileName} already exists and it has {len(self.list)} elements")
        except:
            print(f"{self.fileName} created")
        f.close()
        del f
    def read(self):
        i = None
        i : Persona=(i)
        try:
            f = open(self.fileName,"rb+")
            try:
                with open(self.fileName, 'rb') as f:
                    reader = pickle.load(f)
                if(reader== None):
                    print("Empty file")
                elif(len(reader)==0):
                    print("Empty file")
                for i in reader:
                    print(i.__str__())
                f.close()
                del f
            except:
                print("Error reading file")
        except:
            print(f"{self.fileName} doesnt exist")

    def addList(self, lista):
        self.list.append(lista)
    def saveList(self):
        f = open(self.fileName,"wb+")
        pickle.dump(self.list, f)
        f.close()
        del f
    def cleanList(self):
        self.list.clear()