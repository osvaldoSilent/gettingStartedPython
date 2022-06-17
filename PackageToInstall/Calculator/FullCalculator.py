from .BasicCalculator import BasicCalculator
from .ComplexCalculator import ComplexCalculator
class FullCalculator(BasicCalculator, ComplexCalculator):
    pass
    def __int__(self):
        super().__int__()
