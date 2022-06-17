class Base:
    pass
    #def __int__(self, n):
        #self.data = [ 0 for i in range(n)]
    #def setData(self,n):
        #self.data = [ (int(input(f"Insert data #{(i+1)}:"))) for i in range(n)]
    def __int__(self, n):
        self.data = [ 0 for i in range(n)]
    def setData(self,n):
        self.data = [ (int(input(f"Insert data #{(i+1)}:"))) for i in range(n)]
