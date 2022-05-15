import random
def adivinaUsuario(x):
    randomN=random.randint(1,x)
    prediction=0
    while prediction!=randomN:
        prediction=int(input(f"Ingresa numero entre 1 y {x}: "))
        if prediction<randomN:
            print("jaja es menos perro")
        elif prediction>randomN:
            print("te pasaste we")
    print("limpiate cagado")

def adivinaMaquina(x,y,r):
    inferior = x
    superior = y
    match = 0
    while match != r:
        if match>superior:
            print(f"me pase con {match} pero ya te ando perro")
            superior-=1
        elif match<inferior:
            print(f"me falta con {match} pero ya te ando perro")
            inferior=+1
        match=(random.randint(inferior,superior))
    print(f"El resultado es {match}")

#adivinaUsuario (10)
adivinaMaquina(1,100,int(input("Inserta numero entre 1 y 100: ")))