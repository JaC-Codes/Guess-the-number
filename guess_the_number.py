import random

print("You have 6 attempts!")
numberToGuess = random.randint(1,20)
print(numberToGuess)
stringGuess = input("Guess a number from 1 - 20 ")
intGuess = int(stringGuess)
attempts = 0

while intGuess != numberToGuess and attempts < 6:
    if intGuess < numberToGuess:
        stringGuess = input("Too low guess again! ")
        intGuess = int(stringGuess)
        attempts += 1
    else:
        stringGuess = input("Too high guess again! ")
        intGuess = int(stringGuess)
        attempts += 1


if attempts == 6:
    print("You lost!")
    quit()
if intGuess == numberToGuess:
    attempts += 1
    print("Well done you got it! It took you " + str(attempts) + " attempts!")
