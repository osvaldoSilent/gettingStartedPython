import random
print("funciono perro")

class NumberUserGame:
    response = random.randint(1,100)
    guessed = -1
    while(guessed != response):
        guessed = int(input("Insert a number between 1 and 100: "))
        if(guessed > response):
            print(f"The response expected is smaller than {guessed}\n")
        elif(guessed < response):
            print(f"The response expected is higher than {guessed}\n")
    print(f"\nCongratulations you got it, the response is: {guessed}\n\n\n\n\n\n\n\n\n\n")

class NumberMachineGame:
    print("Setting parameters for game")
    minLimit = int(input("insert min value for game: "))
    maxLimit = int(input("insert mac  value for game: "))
    responseM = random.randint(minLimit,maxLimit)
    print(responseM)
    guessed=-1;
    attempts=0;
    print(f"responseM expected: {responseM}")
    while guessed!=responseM:
        guessed = random.randint(minLimit,maxLimit)
        attempts+=1
        if guessed>responseM:
            print(f"Attemp #{attempts}: The number {guessed} is bigger, let me try again")
            maxLimit=guessed-1;
        elif guessed<responseM:
            print(f"Attemp #{attempts}: The number {guessed} is smaller, let me try again")
            minLimit=guessed+1;

    print(f"The correct responseM: {guessed} was found on the attempt #{attempts}")
    
