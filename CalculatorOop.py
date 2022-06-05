class Calculator:
    def __int__(self,n):
        self.n=n
        self.data=[0 for i in range(n)]
    def setData(self):
        self.data=[int(input("insert number")) for i in range(self.n)]
class BasicCalculator (Calculator):
    def __int__(self,n):
        Calculator.__int__(self,2)
    def suma(self):
        Calculator.setData(self)
        a,b,=self.data
        return print(a+b)
import math;
class AdvancedCalculator (Calculator):
    def __int__(self,n):
        Calculator.__int__(self,1)
    def raiz(self):
        Calculator.setData(self)
        a,=self.data
        return print(int(math.sqrt(a)))

basicCalculator = BasicCalculator();
basicCalculator.__int__(2)
#basicCalculator.suma()

advancedCalculator = AdvancedCalculator();
advancedCalculator.__int__(1)
advancedCalculator.raiz()