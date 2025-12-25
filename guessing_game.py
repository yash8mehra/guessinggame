#Just trying to build a simple guessing game and testing

#NEW THINGS TO ADD
#difficulty levels (number ranges), classes to make it cleaner, highscore tracker per level(later), 

import random

print('WELCOME TO THE GUESSING GAME')
print('ENTER QUIT TO QUIT \n \n \n \n')


class NumberGuessingGame:
    def __init__(self, Min, Max, GuessNum, MaxGuess = None):
        self.Min = Min #This will basically be all 0 anyway but no magic nums
        self.Max = Max #Max Number range
        self.MaxGuess = MaxGuess #none is infinite
        self.RandomNum = random.randint(Min,Max)
        self.GuessNum = GuessNum #how many guesses so far

    def MakeGuess(self, UserNum): #Checking for high/low or out of guesses
        if (self.guesses >= self.MaxGuess) and (self.MaxGuess != None):
            return "No Guess"

        self.GuessNum += 1

        if (UserNum > self.RandomNum):
            return "High"
        elif (UserNum < self.RandomNum):
            return "Low"
        else:
            return "Correct"
        


def ValidInput(play):
    tries = 0 #3 Tries to enter a valid number
    while tries < 3:
        UserNum = input(f"Enter a number between {play.Min} to {play.Max}:          ") #I'll add with variable later

        if UserNum == "QUIT" or UserNum == "quit" or UserNum == "Quit":
            return "QUIT"
    
        if not UserNum.isdigit():
            print("Not a number enter numbers only: ")
            tries += 1
            continue
    

        if int(UserNum) < min or int(UserNum) > max:
            print(f"Number is out of bounds must be between {play.Min} and {play.Max}\n")
            tries += 1
            continue

        if tries >= 3:
            print("Too many attemps")
            return
        
        return int(UserNum) 


         


#main
def main(Min = 0, Max = 100, MaxGuess = None):
    play = NumberGuessingGame(Min, Max, MaxGuess)

    while True:
        UserNum = ValidInput(play)





Guess()
again = "Y"

while again == "Y" or again == "y":
    again = input("\nDo you want to play again? Y/N:   ")

    if again == "Y" or again == 'y':
        Guess()
    else:
        print("\nThankyou for playing with us have a great day!!")





