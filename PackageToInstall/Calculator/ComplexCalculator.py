from .Base import Base
import math

class ComplexCalculator(Base):
    pass
    def __int__(self):
        super().__int__(1)
    def raiz(self):
        self.setData(1)
        a, = self.data
        return math.sqrt(a)
    def square(self):
        self.setData(1)
        a, = self.data
        return math.pow(a,2)
    def cube(self):
        self.setData(1)
        a, = self.data
        return math.pow(a,3)