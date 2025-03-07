# Chandler Hass
# 06 March 2025
# P1HW2

print('This program calculates and displays travel expenses ')
budget = int(input('Enter Budget: '))
destination = input('Enter your travel destination: ')
gas = int(input('how much do you think you will spend on gas? '))
hotel = int(input('Approximately, how much you will need for accomadtion/hotwl? '))
food = int(input('Last, how much do you need for food? '))
print('-----------Travel Expenses____________ ')
print('Location: ', destination)
print('Initial Budget: ', budget)
print()
print('Fuel: ',gas)
print('Accomdation: ',hotel)
print('Food: ',food)
print()
print('Remaining Balance:', budget-gas-hotel-food)