class Calculator:
    def __int__(self, n):
        self.n = n
        self.data = [0 for i in range(n)]

    def setData(self):
        self.data = [int(input(f"Insert number #{i}: ")) for i in range(self.n)]

    def suma(self):
        a, b = self.data
        return print(f"The result of the operation is: {a + b}");


calculator = Calculator()
calculator.__int__(2)
calculator.setData()
calculator.suma()
