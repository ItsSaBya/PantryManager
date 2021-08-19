# The Pantry Manager - Panchan

print()
print("""

The Pantry Manager

Hello, I am Panchan!

1. Pantry
2. Grocery List
3. Exit

""")

pantry = []
grocery = []

panchan = input("How may I help? ")

running = 1
while running == 1:

    if panchan == "1":
        print("This is your Pantry!")
        print(pantry)
        print()
        print("""

        1. Add Item to Pantry
        2. Remove Item from Pantry
        3. Check if Item is on Pantry
        4. Check How Many Items are on Pantry
        5. Clear Pantry
        6. Back to Menu
        
        """)
        print()
    
        p_panchan = 1

        while p_panchan == 1:
            p_panchan = input("What would you like to do? ")

            if p_panchan == "1":

                pantry.append(input("Add Item: "))
                print("Item Added!")
                print()
                print(pantry)

            elif p_panchan == "2":

                pantry.remove(input("Remove Item: "))
                print("Item Removed!")
                print()
                print(pantry)
        
            elif p_panchan == "3":

                wanted_item = input("Find Item: ")

                if wanted_item in pantry:
                    print("Yes, Item is on Pantry")
                else:
                    print("No, Item is not on Pantry")

            elif p_panchan == "4":

                print(len(pantry))

            elif p_panchan == "5":

                confirmation = input("Are you sure? ")
            
                if confirmation == "yes":
                    pantry.clear()
                    print("Pantry Cleaned!")

                if confirmation == "no":
                    pass
            
            elif p_panchan == "6":
                break

            else:
                print("You did not select a Valid Option!")
        
    elif panchan == "2":

        print("This is your Grocery List!")
        print(grocery)
        print()
        print("""

        1. Add Item to Grocery
        2. Remove Item from Grocery
        3. Check if Item is on Grocery
        4. Check How Many Items are on Grocery
        5. Clear Grocery
        6. Back to Menu
        
        """)
        print()

        g_panchan = 1

        while g_panchan == 1:
            g_panchan = input("What would you like to do? ")

            if g_panchan == "1":

                grocery.append(input("Add Item: "))
                print("Item Added!")
                print()
                print(grocery)
                

            elif g_panchan == "2":

                grocery.remove(input("Remove Item: "))
                print("Item Removed!")
                print()
                print(grocery)
        
            elif g_panchan == "3":

                wanted_item = input("Find Item: ")

                if wanted_item in grocery:
                    print("Yes, Item is on Grocery")
                else:
                    print("No, Item is not on Grocery")

            elif g_panchan == "4":

                print(len(grocery))

            elif g_panchan == "5":

                confirmation = input("Are you sure? ")
            
                if confirmation == "yes":
                    grocery.clear()
                    print("Pantry Cleaned!")

                if confirmation == "no":
                    pass
            
            elif g_panchan == "6":
                break

            else:
                print("You did not select a Valid Option! Try Again!")
    
    elif panchan == "3":
        confirmation = input("Are you sure you want to Exit? ")
        if confirmation == "yes":
             running = 0
          
        elif confirmation == "no":
            pass

        else:
            print("Answer ust 'yes' or 'no'. Try Again!")

    else:
        panchan = print("You did not select a Valid Option! Try Again!")

