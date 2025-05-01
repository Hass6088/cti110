# P3LAB_HassChandler
# 28 March 2025
# This program calculates the most efficient way to break down a monetary amount into dollars, quarters, dimes, nickels, and pennies.
amount = float(input("Enter the amount of money as a float: $"))

if amount == 0.00:
    print("no change")
else:
    cents = int(amount * 100)

    dollar = cents // 100
    cents = cents % 100

    quarter = cents // 25
    cents = cents % 25

    dime = cents // 10
    cents = cents % 10

    nickel = cents // 5
    cents = cents % 5

    penny = cents

    if dollar > 0:
        print(f"{dollar} dollar{'s' if dollar > 1 else ''}")
    if quarter > 0:
        print(f"{quarter} quarter{'s' if quarter > 1 else ''}")
    if dime > 0:
        print(f"{dime} dime{'s' if dime > 1 else ''}")
    if nickel > 0:
        print(f"{nickel} nickel{'s' if nickel > 1 else ''}")
    if penny > 0:
        print(f"{penny} penny{'ies' if penny > 1 else ''}")
