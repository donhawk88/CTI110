# Donovan Hawkins
# October 21, 2025
# P3LAB – Branching: Money to Coins
# This program takes a dollar amount and calculates the most efficient number 
# of dollars, quarters, dimes, nickels, and pennies needed to make up that amount.
# It uses integer division and branching to correctly display plural/singular forms.

# Get amount of money from user
amount = float(input("Enter amount of money: "))

# Convert dollars to cents (to avoid floating point rounding issues)
cents = int(round(amount * 100))

# Calculate each denomination
dollars = cents // 100
cents = cents % 100

quarters = cents // 25
cents = cents % 25

dimes = cents // 10
cents = cents % 10

nickels = cents // 5
cents = cents % 5

pennies = cents

# Display the result
if dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
    print("No change")
else:
    if dollars > 0:
        if dollars == 1:
            print(f"{dollars} Dollar")
        else:
            print(f"{dollars} Dollars")

    if quarters > 0:
        if quarters == 1:
            print(f"{quarters} Quarter")
        else:
            print(f"{quarters} Quarters")

    if dimes > 0:
        if dimes == 1:
            print(f"{dimes} Dime")
        else:
            print(f"{dimes} Dimes")

    if nickels > 0:
        if nickels == 1:
            print(f"{nickels} Nickel")
        else:
            print(f"{nickels} Nickels")

    if pennies > 0:
        if pennies == 1:
            print(f"{pennies} Penny")
        else:
            print(f"{pennies} Pennies")
