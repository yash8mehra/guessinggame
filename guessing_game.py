#Just trying to build a simple guessing game and testing

#NEW THINGS TO ADD
#difficulty levels (number ranges), classes to make it cleaner, highscore tracker per level(later), 

import random

print('WELCOME TO THE GUESSING GAME')
print('ENTER QUIT TO QUIT \n \n \n \n')


class NumberGuessingGame:
    def __init__(self, Min, Max, MaxGuess = None):
        self.Min = Min #This will basically be all 0 anyway but no magic nums
        self.Max = Max #Max Number range
        self.MaxGuess = MaxGuess #none is infinite
        self.RandomNum = random.randint(Min,Max)
        self.NumGuess = 0 #how many guesses so far

    def MakeGuess(self, UserNum): #Checking for high/low or out of guesses
        self.NumGuess += 1

        if (self.MaxGuess is not None) and (self.NumGuess >= self.MaxGuess):
            return "No_Guess" #You ran out of guesses :(


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
    

        if int(UserNum) < play.Min or int(UserNum) > play.Max:
            print(f"Number is out of bounds must be between {play.Min} and {play.Max}\n")
            tries += 1
            continue
        
        return int(UserNum)
    print("\nYou got it wrong too many times") 
    return "QUIT"

         


#main
def main(Min = 0, Max = 100, MaxGuess = None):
    play = NumberGuessingGame(Min, Max, MaxGuess)

    while True:
        UserNum = ValidInput(play)
        
        if UserNum == "QUIT":
            print(f'You lose the correct number was {play.RandomNum}')
            return
        
        result = play.MakeGuess(UserNum)
        if result == "No_Guess":
            print(f'You ran out of guesses the correct number was {play.RandomNum}')
            return
        elif result == "Low":
            print("Choose a higher number")
        elif result == "High":
            print("Choose a lower number")
        elif result == "Correct":
            print(f"YAYYYY!! You got it in {play.NumGuess}")
            return
        

        
        




main()
again = "Y"

while again == "Y" or again == "y":
    again = input("\nDo you want to play again? Y/N:   ")

    if again == "Y" or again == 'y':
        main()
    else:
        print("\nThankyou for playing with us have a great day!!")





