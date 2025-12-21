#Just trying to build a simple guessing game and testing
import random



RandomNum = random.randint(1,100)
UserNum = int(input("Enter any number from 0 to 100:          "))
if (UserNum > 100) or (UserNum < 0):
    print("Your number is out of bounds please enter a number from 0 to 100")
else:
    while UserNum != RandomNum:
        if UserNum > RandomNum:
            UserNum = int(input("Your number is too big, enter a smaller one:          "))
        elif UserNum < RandomNum:
            UserNum = int(input("Your number is too small, enter a larger number:           "))  

    if UserNum == RandomNum:
            print("YAY YOU WON THE NUMBER WAS  ", RandomNum)

