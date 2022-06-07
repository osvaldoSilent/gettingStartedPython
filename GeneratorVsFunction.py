class main:

    def __int__(self):
        self.count = 0;
    def funct(self):
        return [2,4,6,8,10];
    def generator(self):
        while(self.count<20):
            self.count+=2
            yield (int(self.count))
        self.count=0


main = main()
main.__int__()
print(main.funct())

algo = main.generator()
print("lista "+str(list(algo)))


list (algo).append(list(main.generator())[0])
print("lista "+str(list(algo)))



print(list(main.generator()))
print(list(main.generator()))
print(list(main.generator()))
print(list(main.generator()))

for i in main.generator():
    print(i)