list = [1,2,3,"perro","gato","caballo",True,"ad"]
tupla = (1,2,3,",","Hola mundo",10.5,True,"asdasd")

diccionario = {
    "Nombre":"Osvaldo",
    "pais":"Mexico",
    "ciudad":"Coacalco",
    "edad":"26",
    "otrosPaises": {"locaciones":["italia","usa","ireland"]}
}

print(diccionario.values())
print(diccionario.keys())
diccionario["nuevo"] = "nuevo"
list.append("ajaja")
print(len(diccionario))
print(len(list))
print(len(tupla))

if ((len(tupla) > len(list) > len(diccionario)) or (len(tupla) == len(list) > len(diccionario))):
    print("true")
else:
    print("false")

print(list)
variable: object
#for variable in list:
#    print("lista "+str(variable))

#for i in range(9):
#    print(i)

for object in tupla:
    print("Tupla: "+str(object))