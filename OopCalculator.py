import math


class Calculator:
    pass

    def setData(self,n):
        self.data = [ 0 for i in range(n)]
        self.data = [ int(input(f"Insert data #{i+1}: ")) for i in range(n)]
class basic_op(Calculator):
    pass
    def suma(self):
        self.setData(2)
        a,b=self.data
        return print(f"Result is {a+b}")
class scientificCalculator(Calculator):
    import math
    pass
    def pow(self):
        self.setData(1)
        a, = self.data
        return print(f"Result is {math.pow(a,2)}")

class CompleteCalculator(basic_op,scientificCalculator):
    pass

    def getOperation(self,n):
        if(n==1):
            basic_op.suma(self)
        elif(n==2):
            scientificCalculator.pow(self)



calculator = CompleteCalculator()
calculator.getOperation(2)
calculator.getOperation(1)
