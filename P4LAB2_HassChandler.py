# Chandler Hass 
# 07 April 2025
# P4Lab2
# this is a program that completes the Times Table

repeat = "yes"

while repeat == "yes":
    
    user_input = input("Enter an integer: ")
    number = int(user_input)  

    if number < 0:
        print("Error: Negative numbers are not accepted. Please run the program again with a non-negative integer.")
    else:
        
        for i in range(1, 13):
            product = number * i
            print(f"{number} * {i} = {product}")
    
    repeat = input("\nWould you like to run the program again? (yes/no): ").strip().lower()
