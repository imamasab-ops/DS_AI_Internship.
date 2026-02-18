# -*- coding: utf-8 -*-
"""
@author: Dell
"""
#task1
# Create a dictionary with at least three contacts
contacts = {
    "Alice": "123-456-7890",
    "Bob": "234-567-8901",
    "Charlie": "345-678-9012"
}
# Add a new contact
contacts["Diana"] = "456-789-0123"
# Update an existing contact's phone number
contacts["Alice"] = "111-222-3333"
# Safe access using .get()
print("Lookup Alice:", contacts.get("Alice"))
print("Lookup Eve:", contacts.get("Eve", "Contact not found"))
print("\nAll Contacts:")
# Iterate through dictionary using .items()
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")

#task2
# Raw login data with duplicates
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
# Convert list to set (removes duplicates automatically)
unique_users = set(raw_logs)
# Membership test
print("Is ID05 in unique users?", "ID05" in unique_users)
# Compare lengths
print("Total log entries:", len(raw_logs))
print("Unique visitors:", len(unique_users))

#task3
# Create two sets
friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
# Intersection (Common interests)
shared_interests = friend_a & friend_b
# Union (All unique interests)
all_interests = friend_a | friend_b
# Difference (Interests friend_a has but friend_b does not)
unique_to_a = friend_a - friend_b
# Output results
print("Shared Interests:", shared_interests)
print("All Interests:", all_interests)
print("Unique to Friend A:", unique_to_a)



