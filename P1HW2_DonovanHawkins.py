# Donovan Hawkins
# 09/28/2025
# P1HW2 – Travel Budget Program
# This program asks the user for their budget, travel destination, and planned expenses.
# It then calculates total expenses and subtracts them from the budget to show the remaining balance.

# ---------------------------------------------------------
# Pseudocode (Logic)
# 1. Ask user to enter their budget
# 2. Ask user to enter travel destination
# 3. Ask user for gas expense
# 4. Ask user for accommodation expense
# 5. Ask user for food expense
# 6. Add gas + accommodation + food to get total expenses
# 7. Subtract total expenses from budget to get remaining balance
# 8. Display destination, expenses, total expenses, and remaining balance
# ---------------------------------------------------------

# Step 1: Ask for user input
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Step 2: Perform calculations
expenses = gas + accommodation + food
remaining_balance = budget - expenses

# Step 3: Display results
print("\n------------Travel Expenses------------")
print("Location:          ", destination)
print("Initial Budget:    $", budget)
print("Fuel:              $", gas)
print("Accommodation:     $", accommodation)
print("Food:              $", food)
print("---------------------------------------")
print("Total Expenses:    $", expenses)
print("Remaining Balance: $", remaining_balance)
