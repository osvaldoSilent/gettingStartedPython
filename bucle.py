count = 0;
while (True):
    count +=1
    if(count==2):
        print("continuing")
        continue
    if(count>5):
        print("passing")
        pass
    print(count)
    if(count==10):
        break;


for i in "al@go":
    print(i)
    if(i == "@"):
        break;
else:
    print("no @")