import math
from calculator import Calculator
class AdvancedCalculator(Calculator.Calculator):
    pass
    def __int__(self):
        super().__int__(1)
    def raiz(self):
        super().setData(1)
        a, = self.data
        return math.sqrt(a)