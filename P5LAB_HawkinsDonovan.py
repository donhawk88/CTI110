# Donovan Hawkins
# 2025-12-05
# P5LAB
# Simulates a self-checkout machine and disperses change in dollars and coins

import random

def disperse_change(change):
    """
    Function to calculate and display the amount of dollars, quarters,
    dimes, nickels, and pennies for a given amount of change.
    """
    # Convert change to cents to avoid floating point errors
    cents = round(change * 100)
    
    dollars = cents // 100
    cents %= 100
    
    quarters = cents // 25
    cents %= 25
    
    dimes = cents // 10
    cents %= 10
    
    nickels = cents // 5
    cents %= 5
    
    pennies = cents
    
    print(f"Change to be given:")
    print(f"Dollars: {dollars}")
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")

def main():
    """
    Main function where the program logic runs:
    - Generates a random total owed
    - Prompts user for payment
    - Calculates change
    - Calls disperse_change() function
    """
    # Generate random amount owed
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Total owed: ${total_owed}")
    
    # Prompt user for cash input
    while True:
        try:
            cash_given = float(input("Enter amount of cash you will put into the self-checkout: $"))
            if cash_given < total_owed:
                print("Error: Cash given must be at least the total owed.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Calculate change owed
    change_owed = round(cash_given - total_owed, 2)
    print(f"Change owed: ${change_owed}")
    
    # Call the disperse_change function
    disperse_change(change_owed)

# Call main function
if __name__ == "__main__":
    main()
