# Conditional if/else logic- these are keywords that instruct your
# program to do specific instructions based on specific data
# or conditions

# conditional syntax (how it is written)
bill_amount = int(input("please type in a bill tender (1,5,10): "))
# if usually indicates that something is possible option
if bill_amount == 1:
        print("here are 4 quaters")

# elif allows us to indicate that there are more possible options
# you can have as many elif as you want
elif bill_amount == 5:
    print("here are 20 quaters")
elif bill_amount == 10:
     print("here are 40 quaters") 
elif bill_amount == 20:
    print("sorry we do not accept 20s. please enter an accepted amount")
elif bill_amount == 50:
    print("sorry we do not accept 50s. please enter an accepted amount")
elif bill_amount == 100:
    print("sorry we do not accept 100s. please enter an accepted amount")     
# else is always your last option
else:
    print("Sorry that type of bill is not accepted")


#create a calculater function that uses if/else lgic to allow the user
# to change or select different arithmetic operations.
# example: an input where if the user enter 1, it will do
# addition, 2 will subtraction
# 3 will do multiplacation

def calculate_add():                    
    print("program has: type in 2 nunmmbers to add")
    num1= int(input())
    num2= int(input())
    print(num1 + num2)
    print("program has ended")

    # phase 2 of function: function call- actualy runs and does something
calculate_add()

def calculate_subtract():                    
    print("program has: type in 2 nunmmbers to subtract")
    num1= int(input())
    num2= int(input())
    print(num1 - num2)
    print("program has ended")
calculate_subtract()    
          

def calculate_multiply():                    
    print("program has: type in 2 nunmmbers to multiply")
    num1= int(input())
    num2= int(input())
    print(num1 * num2)
    print("program has ended")
calculate_multiply()    

def calculate_divide():                    
    print("program has: type in 2 nunmmbers to divide")
    num1= int(input())
    num2= int(input())
    print(num1 / num2)
    print("program has ended")
calculate_divide()    

def mainCalculater():
    selection= input()
    
    if selection == 1:                                
        calculate_add()
    elif selection == 2:
        calculate_subtract()
    elif selection == 3:
          calculate_multiply()
    elif selection == 4:
          calculate_divide()
    else:
        print('sorry somthing went wrong')

def movieTicketPrice():
    print("welcome to the movie theater . How old are you? ")
    age = int(input())
    if age < 7:
        print("your ticket is $8.00")
    elif age > 8 and age < 20:
            print("your ticket is $12.00")
    elif age > 21 and age < 60:
         print("your ticket is $20.00")
    elif age > 61:
         print("your ticket is free")
    else:
            print("sorry invalid input")
    
            
def Signed_permission_slip():
    print("you can go on the trip . what is your gpa?")
    GPA = int(input(What is your GPA))
    if Signed_permission_slip == true:
        print("Oki see your permission slipis signed")
    elif GPA < 90:
            print("your ticket is $12.00")
    elif age > 21 and age < 60:
         print("your ticket is $20.00")
    elif age > 61:
         print("your ticket is free")
    else:
            print("")
   