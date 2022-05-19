

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

    def launchCalculatorMenu(self):
        return int(input(f"The name of the user is {getattr(u,'name')} and is {u.age} years old \n"
                                        f"Chose an option?\n"
                                        f"1-Sumar\n"
                                        f"2-Restar\n"
                                        f"3-dividir\n"
                                        f"4-multiplicar\n"))
    def launchGameMenu(self):
        return int(input(f"Welcome to my APP, what you wanna do? \n"
                         f"What you wanna do?\n"
                         f"1-Set new user\n"
                         f"2-Calculator\n"
                         f"3-Exit\n"))

u = user()
u.default()
u.__int__(10, 2)
optionSelected=0

while(optionSelected!=3):
    optionSelected = u.launchGameMenu()

    if(optionSelected == 1):
        newName = input("insert name for new user: ")
        newAge = input("insert age for new user: ")
        newSex = input("insert sex for new user: ")
        setattr(u,'name',newName)
        setattr(u,'age',newAge)
        setattr(u,'sex',newSex)

    elif(optionSelected == 2):
        optionCalculator=0;
        while(optionCalculator!=5):
            optionCalculator=u.launchCalculatorMenu()
            if(optionCalculator==1):
                print(u.suma+"\n\n\n\n\n")
            elif(optionCalculator==2):
                print(u.resta+"\n\n\n\n\n")
            elif(optionCalculator==3):
                print(u.division+"\n\n\n\n\n")
            elif(optionCalculator==4):
                print(u.multiplication+"\n\n\n\n\n")