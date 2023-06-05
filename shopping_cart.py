# I am utilizing functions in this entire code. So it will be more organized and easier to understand. 

print("Welcome to the Shopping Cart Program!\n ")
def menu(): 
    shopping_cart = []
    while True:
        option = input("""Please select one of the following:
1 - Add item
2 - View cart
3 - Remove item
4 - Compute total
5 - Quit 
Please enter an action: """)

        if option == '1':
            item = add_item(shopping_cart) #calling the function to be executed.
            print(f"{item} has been added to the cart.\n")
        elif option == '2':
            display_contents(shopping_cart)
        elif option == "3":
            remove_item(shopping_cart)
            print("Item removed. \n")
        elif option == "4":
            print(f"The total price of the items in the shopping cart is $ {calculate_total(shopping_cart)}\n")
        elif option == "5":
            print("Thank you. Goodbye.")
            break
        else:
            continue

def add_item(shopping_cart): #this is the function that will be used in the first 'if statement'.
    item = input("What item would you like to add? ")
    price = float(input(f"What is the price of '{item}'? "))
    shopping_cart.append([item, price])
    return item
    

def display_contents(shopping_cart):
    for index, (item, price) in enumerate(shopping_cart, 1):
        print(f"{index}. {item} - ${price} ")
    print()
def remove_item(shopping_cart):
    item = int(input("Which item would you like to remove? "))
    try:     #it will try to execute this code, and if the code gets an error so it will go to the except part.
        position = item - 1
        shopping_cart.pop(position)
    except:   #then will display these message as required. 
        print("Sorry, that is not a valid item number.\n")
    

def calculate_total(shopping_cart):
    index = 0
    total = 0
    for i in shopping_cart:
        total += shopping_cart[index][1]
        index += 1

    return total


menu() #callig the function