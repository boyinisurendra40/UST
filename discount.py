def calculate_trip_cost(km, lpk, ppl):
    fuel = km * lpk
    cost = fuel * ppl
    return cost

km = float(input("Enter kilometers to drive: "))
lpk = float(input("Enter liters per kilometer usage of the car: "))
ppl = float(input("Enter price per liter of fuel (₹): "))

total_cost = calculate_trip_cost(km, lpk, ppl)

print("The total cost of the trip is:", total_cost)

Enter kilometers to drive: 150
Enter liters per kilometer usage of the car: 10
Enter price per liter of fuel (₹): 110
The total cost of the trip is: 165000.0








def calculate_expenses(qty, ppi):
    cost = qty * ppi
    if qty > 10:
        disc = cost * 0.10
        cost -= disc
    return cost

qty = int(input("Enter the quantity of items purchased: "))
ppi = float(input("Enter the price per item (₹): "))

total_cost = calculate_expenses(qty, ppi)

print("The total expenses are: ", total_cost)

"""
Enter the quantity of items purchased: 12
Enter the price per item (₹): 90
The total expenses are:  972.0

"""
