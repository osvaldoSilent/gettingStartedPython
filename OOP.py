class Calculator:
    pass
    def __int__(self, n):
        self.n=n
        self.data = [0 for i in range(n)]
    def setData(self, operation):
        self.data = [ (int(input(f"DATA #{(i+1)} Insert number({operation}): "))) for i in range(self.n)]
class BasicCalculator:
    pass
    def __int__(self):
        Calculator.__int__(self,2)
    def suma(self):
        operation="Suma"
        Calculator.setData(self, operation)
        a,b,=self.data

        return print(f"Result of {operation} is: {(a+b)}")
import math
class ComplexCalculator:
    pass
    def __int__(self):
        Calculator.__int__(self,1)
    def raiz(self):
        operation = "Raiz"
        Calculator.setData(self,operation)
        a, = self.data
        return print(f"Result of {operation} is {int(math.sqrt(a))}")
class FullCalculator(ComplexCalculator,BasicCalculator):
    def __int__(self,complexCalculator,basicCalculator):
        self.complexCalculator = complexCalculator;
        self.basicCalculator = basicCalculator;
        ComplexCalculator.__int__(self.complexCalculator)
        BasicCalculator.__int__(self.basicCalculator)




basicCalculator = BasicCalculator()
basicCalculator.__int__()
#basicCalculator.suma()
complexCalculator = ComplexCalculator()
complexCalculator.__int__()
#complexCalculator.raiz()

fullCalculator = FullCalculator()
fullCalculator.__int__(complexCalculator, basicCalculator)

fullCalculator.basicCalculator.suma()
fullCalculator.complexCalculator.raiz()
fullCalculator.raiz()