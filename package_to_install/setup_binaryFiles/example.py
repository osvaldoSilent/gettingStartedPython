import pickle
class Example:
    pass
    def __int__(self):
        self.name_list=[]
        pass
    def createBinary(self, name):
        f = open(name,"+ab")
        try:
            list = pickle.load(f)
            print(f"Binary file already generated with name {name} and it has {len(list)} lists on it" )
        except:
            print(f"New Binary file created with name: {name}")
        f.close()
        del f;
    def readBinary(self,name):
        fichero = open(name,"rb")
        try:
            name_list = pickle.load(fichero)
            list = pickle.load(fichero)
            print(f"Binary file already generated with name {name} and it has {len(list)} lists on it" )
            for i in list:
                print(i)
        except:
            print(f"Binary file '{name}' is empty")
        fichero.close()
        del fichero
    def addList(self, name, object):
        self.name_list.append(object)
        f = open(name,"+ab")
        f.seek(0)
        pickle.dump(self.name_list,f)
        f.close()
        del f;
