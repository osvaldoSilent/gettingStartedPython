class Calculator:
    pass
    def __int__(self, numberLimit):
        self.numberLimit=numberLimit
        self.data=[0 for i in range(numberLimit)]
    def getNumber(self):
        self.data=[int(input(f"insert number #{i}: ")) for i in range(self.numberLimit) ]
class BasicOperations (Calculator):
    pass
    def __int__(self):
        Calculator.__int__(self,2)
    def sumar(self):
        a,b, = self.data
        print(f"The result of the operation 'Suma' is {a+b}")
    def restar(self):
        a,b, = self.data
        return (a-b)
    def multiplicar(self):
        a,b, = self.data
        return (a*b)
    def dividir(self):
        a,b, = self.data
        return (a/b)



calculator = BasicOperations()
calculator.__int__()
calculator.getNumber()
calculator.sumar()