# -*- coding: utf-8 -*-
"""

@author: Dell
"""
#TASK1 
# Ask for user's name
name = input("Enter your name: ")
# Ask for current age
age = input("Enter your current age: ")
# Convert age to integer
age = int(age)
# Calculate age in 2030 (2026 + 4 years)
age_2030 = age + 4
# Display result
print("\nHello", name + "!")
print("You will be", age_2030, "years old in 2030.")

#task2
# Ask for total bill amount (float for decimals)
total_bill = float(input("Enter the total bill amount: "))
# Ask for number of people
num_people = int(input("Enter the number of people: "))
# Calculate share per person
share_per_person = total_bill / num_people
# Print result (rounded to 2 decimal places)
print(f"\nTotal Bill: {total_bill}")
print(f"Each person pays: {share_per_person:.2f}")


#task3
# Hardcoded variables
item_name = "Laptop"      # String
quantity = 2              # Integer
price = 499.99            # Float
in_stock = True           # Boolean
# Print formatted receipt using commas
print("Item:", item_name, ", Qty:", quantity, ", Price:", price, ", Available:", in_stock)
# Calculate total cost
total_cost = quantity * price
# Print total cost
print("Total Cost:", total_cost)
