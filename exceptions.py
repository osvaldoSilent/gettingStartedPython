command="";
while(True):
    command=input("Insert a number")
    if(command == "Exit"):
        break
    try:
        int(command)
        print("its an int")
    except ValueError:
        print("pls insert a number")
    try:
        float(command)
        print("Its a float")
    except ValueError:
        print("pls insert a number")


    if(isinstance(command,str)):
        print("esto es un string perri")

        if(command in "Exit"):
            print("Te saliste perri")