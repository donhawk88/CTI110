# Donovan Hawkins
# October 21, 2025
# P2HW2 - List Grades
# This program asks the user to enter six module grades,
# stores them in a list, and then displays the lowest grade,
# highest grade, sum, and average of the grades.

# Pseudocode:
# 1. Ask the user to enter grades for Module 1 through Module 6.
# 2. Store the grades entered in a list named grades_list.
# 3. Display the following:
#    - Lowest grade
#    - Highest grade
#    - Sum of grades
#    - Average of grades
# 4. Format all numeric values to two decimal places where needed.

# Ask the user to input grades
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

# Store grades in a list
grades_list = [mod1, mod2, mod3, mod4, mod5, mod6]

# Display results
print("\n------------ Results ------------")
print(f"{'Lowest Grade:':<20} {min(grades_list):.2f}")
print(f"{'Highest Grade:':<20} {max(grades_list):.2f}")
print(f"{'Sum of Grades:':<20} {sum(grades_list):.2f}")
print(f"{'Average:':<20} {sum(grades_list) / len(grades_list):.2f}")
print("----------------------------------")
