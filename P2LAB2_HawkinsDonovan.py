# Donovan Hawkins
# 10/08/2025
# P2LAB2
# This program uses a dictionary to store vehicle MPG values,
# displays available vehicles, prompts the user for a vehicle
# and miles to drive, and calculates the gallons of gas needed.

# Create the dictionary
vehicle_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Get all keys from the dictionary
keys = vehicle_mpg.keys()

# Display the keys
print("Available vehicles:", keys)

# Prompt the user for a vehicle
vehicle = input("Enter a vehicle from the list above: ")

# Check if the vehicle is in the dictionary
if vehicle in vehicle_mpg:
    mpg = vehicle_mpg[vehicle]
    print(f"{vehicle} has an MPG of {mpg}")
    
    # Prompt for number of miles to drive
    miles = float(input(f"Enter the number of miles you will drive the {vehicle}: "))
    
    # Calculate gallons needed
    gallons_needed = miles / mpg
    
    # Display gallons needed rounded to two decimal places
    print(f"You will need {gallons_needed:.2f} gallons of gas to drive {miles} miles in a {vehicle}.")
else:
    print("Vehicle not found in the dictionary. Make sure you typed it exactly as shown.")
