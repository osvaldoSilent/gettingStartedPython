from calculator import Calculator
class BasicCalculator(Calculator.Calculator):
    pass
    def __int__(self):
        super().__int__(2)
    def suma(self):
        super().setData(2)
        a,b, = self.data
        return (a+b)