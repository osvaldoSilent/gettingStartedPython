

class user:
    def default(self):
        self.name="Osvaldo"
        self.sex="M"
        self.age=25

    def __int__(self,n1,n2):
        self.suma=n1+n2
        self.resta=n1-n2
        self.division=n1/n2
        self.multiplication=n1*n2



u = user()
u.default()
u.__int__(10,2)
print(f"The name of the user is {u.name} and is {u.age} years old");
print(u.suma)
print(u.resta)
print(u.division)
print(u.multiplication)