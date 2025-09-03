import random
num = random.randint(1,100)
i = 1
while True:
    num2 = int(input("Guess a number between 1 and 100: "))
    if num2 < num :
        print("too low, try again")
    elif num2 > num :
        print("too high, try again")
    else :
        print("congratulations, you guessed it!")
        break
    i += 1
print(f"You guessed it in {i} tries!")
    