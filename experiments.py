class encapsulated:
    pass
    def __int__(self):
        self.__name= "Osvaldo"
        self.__age= 26
        self.__assignoTHERS()
    def __assignoTHERS(self):
        self.pet="cali"

enca = encapsulated()
enca.__int__()
print(enca.pet)