# what is loops --> Code that repeats>

#while loops is a block code that repeats itself untill Triggering
#condition is no longer True> CAN BE INFINITE

# For loops - a type of loop (code block repeats itself)


















#fooditem1+"popcorn"

#grocerylist = ["popcorn", "apples", "water", "chips","fish","celery"]

#for 1 in grocerylist:
#    print("i need to buy" + str(1))
#Itemprices = [10.00, 20,00,13.25,7.95,349.00]
#tax = 0.07

#for 1 in Itemprices:
    # i want to know how much in taxes i need to pay on each item
    #print("you will pay this in taxes" + str(tax * 1))

#semestergrades = [90,100,78,76,74,82,84]

#for 1 in semestergrades:
    # I want to know all the grades lower than 85
    #if i < 85:
        #print(i)

# Lists - keep our data structured abd organized

#Drinks = []
#sandwichs []
#soups = []
#wawa_kisosk = drinks, sandwichs, soups

#when select an item,we use the indexing system of a list
inventory = [ "weapon","healing kit","armor","grenade"]

#lists are 0 based indexing systems, MEANING- the first item
#in a list starts with 0
print(inventory[0])

# Lists are also changable and manipulateable (mutable)

#when we want to add items we use the append() method

inventory.append("knife")
print(inventory)

inventory.remove("healing kit")
inventory.insert(3, "healing kit")

print(inventory)