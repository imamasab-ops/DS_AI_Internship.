# -*- coding: utf-8 -*-
"""
@author: Dell
"""
#task1
# Create the inventory list
inventory = ["Apples", "Bananas", "Carrots", "Dates"]
# Print current inventory
print("Current Inventory:", inventory)
# Add "Eggs" to the inventory
inventory.append("Eggs")
# Remove "Bananas" from the inventory
inventory.remove("Bananas")
# Sort inventory alphabetically
inventory.sort()
# Print final updated inventory
print("Final Updated Inventory:", inventory)

#Task2
# Create the list of temperature readings
temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
# Print first and last readings
print("First Reading:", temperatures[0])
print("Last Reading:", temperatures[-1])
# Extract Afternoon Peak (4th, 5th, 6th items)
afternoon_peak = temperatures[3:6]
print("Afternoon Peak Readings:", afternoon_peak)
# Extract Last 3 Hours
last_three = temperatures[-3:]
print("Last 3 Hours Readings:", last_three)

#task3
# Create a tuple for screen resolution
screen_res = (1920, 1080)
# Print current resolution
print(f"Current Resolution: {screen_res[0]}x{screen_res[1]}")
# The Experiment (This will cause a TypeError)
print("Tuples cannot be modified!")




