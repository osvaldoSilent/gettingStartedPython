from .Base import Base
class BasicCalculator(Base):
    pass
    def __int__(self):
        super().__int__(2)
    def sume(self):
        self.setData(2)
        a,b, = self.data
        return a + b;
    def rest(self):
        self.setData(2)
        a,b, = self.data
        return a - b;
    def divition(self):
        self.setData(2)
        a,b, = self.data
        return a / b;
    def multiplication(self):
        self.setData(2)
        a,b, = self.data
        return a * b;