items = [
    ["Bread", 40],
    ["Cookies", 80],
    ["Butter", 120],
    ["Cheese", 180],
    ["Yoghurt", 60]
]


cart = []

while True:
    print("\nWhat do you want to do?")
    print("1. View items")
    print("2. Add items to cart")
    print("3. Update items in cart")
    print("4. Delete items from cart")
    print("5. Print bill")
    print("6. Exit")

    choice_input = input("Enter your choice: ")
    
    if choice_input.isdigit():
        choice = int(choice_input)
        
        if choice == 1:
            print("Items Available:")
            for item in items:
                print(f"Name: {item[0]} Price: {item[1]}")

        elif choice == 2:
            item_name = input("Enter the item name: ").capitalize()
            item_found = False
            for item in items:
                if item[0] == item_name:
                    quantity = input("Enter the quantity: ")
                    if quantity.isdigit():
                        quantity = int(quantity)
                        cart.append([item_name, quantity, item[1], quantity * item[1]])
                        print(f"{item_name} added to the cart.")
                    else:
                        print("Invalid quantity.")
                    item_found = True
                    break
            if not item_found:
                print("Item not found.")

        elif choice == 3:
            item_name = input("Which item to be updated: ").capitalize()
            item_found = False
            for cart_item in cart:
                if cart_item[0] == item_name:
                    new_quantity = input("Enter the new quantity: ")
                    if new_quantity.isdigit():
                        new_quantity = int(new_quantity)
                        cart_item[1] = new_quantity
                        cart_item[3] = new_quantity * cart_item[2]
                        print(f"Updated quantity for {item_name}.")
                    else:
                        print("Invalid quantity.")
                    item_found = True
                    break
            if not item_found:
                print("Item not found in cart.")

        elif choice == 4:
            item_name = input("Which item to be removed: ").capitalize()
            item_found = False
            for i, cart_item in enumerate(cart):
                if cart_item[0] == item_name:
                    cart.pop(i)
                    print(f"{item_name} removed from cart.")
                    item_found = True
                    break
            if not item_found:
                print("Item not found in cart.")

        elif choice == 5:
            print("Name, Quantity, Price, Total")
            total_amount = 0
            for item_name, quantity, price, total in cart:
                print(f"{item_name}, {quantity}, {price}, {total}")
                total_amount += total
            print(f"Total Amount of Bill: {total_amount}")

        elif choice == 6:
            print("Thank you for shopping!")
            break

        else:
            print("Invalid choice. Please try again.")
    else:
        print("Invalid input. Please enter a number.")
