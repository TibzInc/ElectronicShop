import sys

def addItem():
    nItem = input("\nWhat is the product name?\n")
    nPrice = input("\nWhat is the product price?\n")

    f = open("Shop.txt","a") #save to text file
    total = nItem + "," + str(nPrice) + "\n"
    f.write(total)
    f.close()

    print("SUCCESSFUL...\nProducts added to inventory\n")

    ReturnToMenu() #Return to the main menu

def findItem():
    content = []
    pProduct=[]
    itemFound = False
    
    f = open("Shop.txt","r") #read products in text file
    content = f.readlines()
    fItem = str(input("Search product:"))
    for i in content:
        if fItem in i: #check for item
            itemFound = True
            pProduct = i.split(",")
            print("Product name: " + pProduct[0])
            print("Price: " + pProduct[1])

    if itemFound == False:
        print("Product not found. Try again?")
    f.close()

    ReturnToMenu() #Return to the main menu

def inventory():
    count = 0
    
    f = open("Shop.txt","r")#count items in file
    inventorycontent = f.readlines()
    print("\nThese are the list of current products:\n")
    for j in inventorycontent:
        count = count +1

        iInventory = j.split(",")
        print(str(count) + ". " + iInventory[0])
        
    print("Current total number of products in the inventory: " + str(count) + "\n")
    f.close()

    ReturnToMenu() #Return to the main menu
    
def chooseAction():
    print("Welcome to Tib'z Electronics")
    print("[1] Add Product")
    print("[2] Find Product")
    print("[3] Inventory")
    print("[4] Exit")

    response = int(input("\nWhich area of the store do you want to go? "))
    if response == 1:
        addItem()
    elif response == 2:
        findItem()
    elif response == 3:
        inventory()
    elif response == 4:
        print("Thanks for coming to Tib'z Electronics")
        sys.exit()
        
    else:
        print("Try again..")
        chooseAction()

def ReturnToMenu():
    menuExit = False
    
    print("\n\n")
    Returnmenuresponse = str(input("Return to Main Menu (Press Y)"))
    if Returnmenuresponse == "Y":
        menuExit = True
        chooseAction()
    else:
        print("Incorrect input..")
        ReturnToMenu()
        
#main

chooseAction() #Start the Electronic Shop


