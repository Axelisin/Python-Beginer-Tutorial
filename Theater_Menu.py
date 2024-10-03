# theater menu program - using dictionary (menu)

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "soda": 2.00,
        "coca-cola": 3.50,
        "lemonade": 4.50}

cart = []
total = 0

print("------- MENU -------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------------")

while True:
    food = input("Select an item from the menu (q to quit): ").lower()
    #print()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("----- YOUR ORDR -----") 
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
    
print()
print(f"Total is: ${total:.2f}")