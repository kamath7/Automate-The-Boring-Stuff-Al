#Lalle Guess a number game
import random 

print("Welcome to the game. Guess the number I have selected from 1 to 10")
numberOfChances = 0
randomNum = random.randint(1,10)
while True:
    guess = int(input("Enter your number "))
    if guess == randomNum:
        print("You guessed it")
        numberOfChances = numberOfChances + 1
        break
    elif guess < randomNum:
        print("You need to think higher")
        numberOfChances = numberOfChances + 1
    elif guess > randomNum:
        print("Think lower.")
        numberOfChances = numberOfChances + 1        

    if numberOfChances == 6:
        print("You have consumed all your chances to guess")
        break
print("You took {0} chances to guess".format(numberOfChances,))