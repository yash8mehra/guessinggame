#Just trying to build a simple guessing game and testing

#NEW THINGS TO ADD
#Guess counter(done), quit option(Done), replay without restarting(play again button done), difficulty levels (number ranges)

import random

print('WELCOME TO THE GUESSING GAME')
print('ENTER QUIT TO QUIT \n \n \n \n')


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





