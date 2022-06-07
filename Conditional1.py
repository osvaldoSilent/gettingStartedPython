correo = "osvald.silent@gmail.com"
count = 0
state = False;

for i in correo:
    if(i=="@"):
        count=count+1;
    elif(i=="." and count == 1):
        count = count +1;

print(count==2)