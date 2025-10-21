# Donovan Hawkins
# 10/21/2025
# P2HW1 Assignment
# This program takes travel destinations and amounts from the user
# and displays them in a nicely formatted table with aligned columns
# and dollar amounts with two decimal places.

# Number of destinations to collect
num_destinations = int(input("How many travel destinations would you like to enter? "))

# Lists to store destinations and amounts
destinations = []
amounts = []

# Collect data from user
for i in range(num_destinations):
    dest = input(f"Enter destination {i + 1}: ")
    amt = float(input(f"Enter amount to {dest}: $"))
    destinations.append(dest)
    amounts.append(amt)

# Display formatted output
print("\nTravel Budget Summary")
print("=" * 40)
print(f"{'Destination':<20} {'Amount':>15}")
print("-" * 40)

# Loop through data and display each row
for i in range(num_destinations):
    print(f"{destinations[i]:<20} ${amounts[i]:>14.2f}")

# Total amount
total = sum(amounts)
print("-" * 40)
print(f"{'Total':<20} ${total:>14.2f}")
