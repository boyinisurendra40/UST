items = [
    ['Bread', 40],
    ['Cookies', 80],
    ['Butter', 120],
    ['Cheese', 180],
    ['Yoghurt', 60]
]

cart = []

def display_items():
    print("Items available:")
    for item in items:
        print(f"Name: {item[0]} Price: {item[1]}")

def add_to_cart():
    item_name = input("Enter the item name: ")
    for item in items:
        if item[0] == item_name:
            quantity = int(input("Enter the quantity: "))
            for entry in cart:
                if entry[0] == item_name:
                    entry[1] += quantity
                    entry[3] = entry[1] * entry[2]
                    return
            cart.append([item_name, quantity, item[1], quantity * item[1]])
            return
    print("Item not available.")

def update_cart():
    item_name = input("Which item to be updated: ")
    for entry in cart:
        if entry[0] == item_name:
            quantity = int(input("Enter the quantity to be updated: "))
            entry[1] = quantity
            entry[3] = entry[1] * entry[2]
            return
    print("Item not in cart.")

def delete_from_cart():
    item_name = input("Which item to be removed: ")
    for entry in cart:
        if entry[0] == item_name:
            cart.remove(entry)
            return
    print("Item not in cart.")

def print_bill():
    print("Name,Quantity,Price,Total")
    total_amount = 0
    for entry in cart:
        print(f"{entry[0]},{entry[1]},{entry[2]},{entry[3]}")
        total_amount += entry[3]
    print(f"Total Amount of Bill {total_amount}")

while True:
    print("\nWhat do you want to do?")
    print("Enter 1 for viewing the items")
    print("Enter 2 for adding the items in cart")
    print("Enter 3 for updating the items in cart")
    print("Enter 4 for deleting the items in cart")
    print("Enter 5 for printing bill")
    print("Enter 6 to exit")

    choice = int(input("Enter the choice: "))

    if choice == 1:
        display_items()
    elif choice == 2:
        add_to_cart()
    elif choice == 3:
        update_cart()
    elif choice == 4:
        delete_from_cart()
    elif choice == 5:
        print_bill()
    elif choice == 6:
        break
    else:
        print("Invalid choice. Try again.")
