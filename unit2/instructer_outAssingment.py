import random

print(random.randint(1, 7))


def diceGame():
    print("DICE GAME")
    print("type R to roll the dice or Q to quit games")
    userselection = input()

    while userselection != 'q':
        if userselection == "r":
            diceValue == random.randint(1,7))
            if dicevalue == 7:
            print("type R to roll the dice or Q to quit the game: ")
            userselection = input()
        else:
            print("you rolled a: " + str(diceValue))
            print







#returns a number between 1 and 7 (both included)
#use input to allow user to enter a value
#values are r for roll and q for quit

#loop = r to keep playing q to stop loop

#if they enter r, give random number between 1 and 7

#if they roll 7 get 10 pints choose to keep rolling

#if they roll anything else lose 5 points, choose to 
#keep rolling


