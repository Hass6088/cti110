#Chandler Hass
# 01 may 2025
# 5HW
# This is a character create game

import random


def create_character():
    name = input("Enter your character's name: ")
    health = 250
    attack = random.randint(25, 100)
    character = {
        "name": name,
        "health": health,
        "attack": attack
    }
    return character


def display_character(character):
    print("\nCharacter Info:")
    for key, value in character.items():
        print(f"{key.capitalize()}: {value}")


def battle(character1, character2):
    print(f"\n{character1['name']} and {character2['name']} are battling!\n")
    
    
    while character1['health'] > 0 and character2['health'] > 0:
        
        damage1 = random.randint(0, character1['attack'])
        character2['health'] -= damage1
        print(f"{character1['name']} attacks {character2['name']} for {damage1} damage!")
        
        
        if character2['health'] > 0:
            damage2 = random.randint(0, character2['attack'])
            character1['health'] -= damage2
            print(f"{character2['name']} attacks {character1['name']} for {damage2} damage!\n")
        
        
        print(f"{character1['name']} Health: {character1['health']}")
        print(f"{character2['name']} Health: {character2['health']}\n")
        
        
        input("Press Enter to continue to the next turn...\n")
    
    if character1['health'] <= 0:
        print(f"{character1['name']} has been defeated! {character2['name']} wins!")
    elif character2['health'] <= 0:
        print(f"{character2['name']} has been defeated! {character1['name']} wins!")


def main():
    print("Welcome to the Character Creation Game!")
    character = create_character()

    while True:
        print("\nWhat would you like to do?")
        print("1. Show character info")
        print("2. Battle an enemy")
        print("3. Exit game")

        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            display_character(character)
        elif choice == "2":
            if character["health"] <= 0:
                print("Your character has no health left! Game over.")
                break
            
            
            enemy = create_character()
            display_character(enemy)
            battle(character, enemy)
        elif choice == "3":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
