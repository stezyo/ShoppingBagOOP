from ShoppingBag import ShoppingBag
test = ShoppingBag()

while True:

    print("""
    Shopping Bag Options
    --------------------
    1. Add Item
    2. Remove Item
    3. View Bag
    4. Exit
"""
)
    selection = input("Make a selection: ")

    if selection == 1:
        choice = str(input("What would you like to add?: "))
        test.addToBag(choice)        

    elif selection == 2:
        print("Current Items: ")
        test.showBag()    
        toDel = str(input(f"Select item to remove: "))
        test.removeFromBag(toDel)

    elif selection == 3:
        test.showBag()
        
    elif selection == 4:
        print("quit")

    else: 
        print (f"I don't understand")
