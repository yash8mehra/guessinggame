#Just trying to build a simple guessing game and testing

#NEW THINGS TO ADD
#Guess counter(done), quit option, replay without restarting, difficulty levels (number ranges)

import random

print('WELCOME TO THE GUESSING GAME')
print('ENTER ANY LETTER TO QUIT \n \n \n \n')


def guess():
    RandomNum = random.randint(1,100)
    print(RandomNum)
    UserNum = int(input("Enter any number from 0 to 100:          "))
    NumGuesses = 1
    while UserNum != RandomNum:
        NumGuesses += 1
        if (UserNum > 100) or (UserNum < 0):
            print("Your number is out of bounds game over")
            break
        
        elif not type(UserNum) is int:
            raise TypeError("Awww sorry you had to quit \n")
            break



        else:  
        
            if UserNum > RandomNum:
                UserNum = int(input("Your number is too big, enter a smaller one:          "))

            elif UserNum < RandomNum:
                UserNum = int(input("Your number is too small, enter a larger number:           "))



    if UserNum == RandomNum:
            print("YAY YOU WON THE NUMBER WAS:  ", RandomNum, ". It took you ", NumGuesses, " guesses")
    else:
        print("YOU LOSE SORRY!! THE RIGHT NUMBER WAS:  ", RandomNum)
         

guess()
again = "Y"

while again == "Y" or again == "y":
    again = input("\nDo you want to play again? Y/N:   ")

    if again == "Y" or again == 'y':
        guess()
    else:
        print("\nThankyou for playing with us have a great day!!")





