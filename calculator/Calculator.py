class Calculator:
    pass
    def __int__(self,n):
        self.data = [0 for i in range(n)]
    def setData(self,n):
        self.data=[ int(input("Insert number: ")) for i in range(n) ]

class BasicCalculator(Calculator):
    pass
    def __int__(self):
        super().__int__(2)
    def suma(self):
        super().setData(2)
        a,b, = self.data
        return (a+b)
import math
class AdvancedCalculator(Calculator):
    pass
    def __int__(self):
        super().__int__(1)
    def raiz(self):
        super().setData(1)
        a, = self.data
        return math.sqrt(a)
class FullCalculator(BasicCalculator, AdvancedCalculator):
    pass
    def __int__(self):
        pass


