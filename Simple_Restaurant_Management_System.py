menu = {
    "Coffee": 2.5,
    "Pasta" : 4.5,
    "Burger": 5.0,
    "Salad": 3.0,
    "Wrap" : 4.0
}

print(
    '''
    Welcome to the Simple Restaurant Management System
    Here is the menu:
    Coffee - $2.50
    Pasta - $4.50
    Burger - $5.00
    Salad - $3.00
    Wrap - $4.00
    '''
)

total_price = 0

choice = " "
print("Welcome to Restaurant Management System!")
while True:
    choice = input("Enter the name of the item you want to order: ")
    if choice in menu:
        total_price +=menu[choice]
        print(f"You have ordered {choice}. The total order price is {total_price} ")
        print('''Do you want to order something else?
                Enter 1 for yes
                Enter 2 for no
            ''')
        if int(input()) == 1:
            continue
        else:
            break
    else:
        print(f"Sorry {choice} not avaialable. Please order something else from the menu")
print(f"Thank you. Your total is {total_price}")    #The else: after while True: runs only if the loop exits without break — not what you want here.






# item1 = input("Enter the name of the item you want to order")

# if item1 in menu:
#     total_price +=menu[item1]
#     print(f"You have ordered {item1}.Total order price is {total_price}")
# else:
#     print(f"Sorry! {item1} is unavailable")
#     print("Please choose another item from the menu.")

# another_order = input("Do you want to order another item? (yes/no): ")

# if another_order.lower() == "yes":
#     item2 = input("Enter the name of the item you want to order")
#     if item2 in menu:
#         total_price += menu[item2]
#         print(f"You have ordered {item2}. Total order price is {total_price}")
#     else:
#         print(f"Sorry! {item2} is unavailable")
#         print("Please choose another item from the menu.")
        
# print(f"The total amount is {total_price}. Thank you for ordering")