# Donovan Hawkins
# 10/08/2025
# P2LAB1
# This program asks the user for the radius of a circle,
# then calculates and displays the diameter, circumference,
# and area with the correct formatting.

import math

# Ask user for radius
radius = float(input("Enter the radius of the circle: "))

# Perform calculations
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

# Display results with required formatting
print(f"Diameter: {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")
