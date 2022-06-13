from .BaseCalculator import BaseCalculator
import math

class ComplexOperation(BaseCalculator):
    pass
    def __int__(self):
        super().__int__(1)
        pass
    def raiz(self):
        self.setData(1)
        a,=self.data
        return math.sqrt(a)
    def cuadrado(self):
        self.setData(1)
        a,=self.data
        return math.pow(a,2)
    def cubo(self):
        self.setData(1)
        a,=self.data
        return math.pow(a,3)