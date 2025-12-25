#Just trying to build a simple guessing game and testing

#NEW THINGS TO ADD
#difficulty levels (number ranges), classes to make it cleaner, highscore tracker per level(later), 

import random

print('WELCOME TO THE GUESSING GAME')
print('ENTER QUIT TO QUIT \n \n \n \n')


class NumberGuessingGame:
    def __init__(self, Min, Max, GuessNum):
        self.Min = Min #This will basically be all 0 anyway but we dont want magic numbers :)
        self.Max = Max
        self.GuessNum = GuessNum
        #Bottom are determined by the game Top are determined by the user
        self.RandomNum = random.randint(Min,Max)
        self.guesses = 0
        


def ValidInput():
    tries = 0 #3 Tries to enter a valid number
    while tries < 3:
        UserNum = input("Enter any number from 0 to 100:          ")

        if UserNum == "QUIT" or UserNum == "quit" or UserNum == "Quit":
            return "QUIT"
    
        if not UserNum.isdigit():
            print("Not a number enter numbers only: ")
            tries += 1
            continue
    

        if int(UserNum) < 0 or int(UserNum) > 100:
            print("Number is out of bounds must be between 0 and 100\n")
            tries += 1
            continue

        if tries >= 3:
            print("Too many attemps")
            return
        
        return int(UserNum) 




def Guess():
    RandomNum = random.randint(1,100)
    print(f'random number is {RandomNum}') #For debugging purposes

    NumGuesses = 0


    while True:
        UserNum = ValidInput()
        if UserNum is None:
            print("Game over, too many wrong attemps")
            return
        
        elif UserNum is "QUIT":
            print(f"Sorry you quit, the right number was {RandomNum}")
            return
        
        NumGuesses += 1

        if UserNum > RandomNum:
            print("Too high")
        elif UserNum < RandomNum:
            print("Too low")
        else:
            print(f"YAY YOU WON THE NUMBER WAS:  {RandomNum}. It took you  {NumGuesses} guesses")
            return

         

Guess()
again = "Y"

while again == "Y" or again == "y":
    again = input("\nDo you want to play again? Y/N:   ")

    if again == "Y" or again == 'y':
        Guess()
    else:
        print("\nThankyou for playing with us have a great day!!")





