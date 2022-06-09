class Calculator:
    pass
    def __int__(self,n):
        self.data = [0 for i in range(n)]
    def setData(self,n):
        self.data=[ int(input("Insert number: ")) for i in range(n) ]
