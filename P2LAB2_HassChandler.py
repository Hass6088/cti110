# Chandler Hass
# 03/09/2025
# P2LAB2
# This program uses a dictionary to store vehicle MPG and calculates the gallons of gas needed based on user input.

car_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}
print("dict_keys(['Camaro', 'Prius', 'Model S', 'Silverado'])")

print()
vehicle = input("Enter a vehicle to see its mpg: ")
mpg = car_mpg.get(vehicle)

print()

print("The", vehicle, "gets", mpg, "mpg.")
print()

miles = input("How many miles will you drive the " + vehicle + "? ")
gallons_needed = float(miles) / mpg

print()

print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")
