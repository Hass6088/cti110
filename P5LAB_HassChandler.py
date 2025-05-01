# Chandler Hass
# 20 April 2025
# P5Lab 
# Self-Checkout Simulator/Calculator

import random

def disperse_change(change):
    cents = round(change * 100)
    
    dollars = cents // 100
    cents = cents % 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5
    cents = cents % 5

    pennies = cents
    
    print("\nChange breakdown:")
    if dollars > 0:
        print(dollars, "Dollars")
    if quarters > 0:
        print(quarters, "Quarters")
    if dimes > 0:
        print(dimes, "Dimes" )
    if nickels > 0:
        print(nickels, "Nickels" )
    if pennies > 0:
        print(pennies, "Pennies")

def main():
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print("You owe: $", total_owed)

    amount_given = float(input("How much cash will you put in the self-checkout?  "))

    if amount_given < total_owed:
        print("Insufficient amount. Please enter enough to cover the total.")
    else:
        change = round(amount_given - total_owed, 2)
        print("Change is: $", change)
        disperse_change(change)

main()
