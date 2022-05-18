

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
        self.launchMenu=int(input(f"The name of the user is {u.name} and is {u.age} years old \n"
                                        f"What you wanna do?\n"
                                        f"1-Sumar\n"
                                        f"2-Restar\n"
                                        f"2-dividir\n"
                                        f"2-multiplicar\n"))


u = user()
u.default()
u.__int__(10,2)

option = u.launchMenu
if(option==1):
    print(u.suma)
elif(option==2):
    print(u.resta)
elif(option==3):
    print(u.division)
elif(option==4):
    print(u.multiplication)