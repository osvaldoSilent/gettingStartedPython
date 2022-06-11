from package_to_install.setup_package.BaseCalculator import BaseCalculator

class BasicOperation(BaseCalculator):
    pass
    def __int__(self):
        super().__int__(2)
    def sumar(self):
        self.setData(2)
        a,b, = self.data
        return a+b
    def restar(self):
        self.setData(2)
        a,b, = self.data
        return a-b
    def multiplicar(self):
        self.setData(2)
        a,b, = self.data
        return a*b
    def dividir(self):
        self.setData(2)
        a,b, = self.data
        return a/b
