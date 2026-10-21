#loop - a loop is aconstruct (special function) that repeats itself
#In programming, a loop allows to repeat code instructions

#There are two types of loops: for loop and while loop

#while loop - a type where so long as a condition is equal
#to true it will keep running "running"

#the keyboard --> do while

#syntax
num = 4
while 2+2 == num: #condition --> operations - must be TRUE
    print("the program is running...")
    num=int(input("please type in a number"))

# While loops will ALWAYS run unless you change the condition!
# we can do this by writing instructions to manually change it.


def guessingGame():
    correctanswer = 12
    attempts = 0

    print("GUESSING HAS STARTED")
    userguess = input("Please guess a number between 1 and 50")

    while userGuess != correctAnswer:
        print("inccorect please try again...")
        attempts +=1
        print("guess attempts: " + str(attempts)
        userGuess = int(input("please guess a number between 1 and 50"))

    print("you guessed correct lil nigy")

guessingGame():


def passwordreset():
    correctpassword = 6656
    attempts = 4

    print("PASSWORD reset has started")
    userguess = input("Guess the four numbers of the password")

    while userGuess != correctpassword:
          print("inccorrect please try again")
          attempts +=1
          print("guess attepmts:" + str(attempts)
          userguess = int(input("please guess the right password 6656") 

       print("you guesses correct kid")