# Chandler Hass
# 03/16/2025
# P2HW1
# This program is to see what your vaction budget you will need for vaction

print('This program calculates and displays travel expenses')
print()
budget = float(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas? "))
print()
hotel = float(input("Approximately, how much will you need for accommodation/hotel? "))
print()
food = float(input("Last, how much do you need for food? "))
print()

total_expenses = gas + hotel + food
remaining_balance = budget - total_expenses

print("\n-----------Travel Expenses------------")
print(f"Location: {destination}")
print(f"Initial Budget: ${budget:.2f}")
print(f"Fuel: ${gas:.2f}")
print(f"Accommodation: ${hotel:.2f}")
print(f"Food: ${food:.2f}")
print("----------------------------------------")
print()
print(f"Remaining Balance: ${remaining_balance:.2f}")