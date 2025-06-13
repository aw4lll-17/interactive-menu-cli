import sys
import os
import time
from colorama import init, Fore, Style

init(autoreset=True)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Initial screen clear and welcome message
clear_screen()
time.sleep(1)
print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "--- Stage 5 : Interactive Menu using Def ---")
time.sleep(2)

# Get user's name (moved up to be executed once at the start)
name = input(Fore.YELLOW + "Please insert your name: " + Style.RESET_ALL)

# Initialize user_data list here, before any function tries to use it
user_data = []

def age_checking(name):
    try:
        age_str = input(Fore.YELLOW + "Insert your age: " + Style.RESET_ALL)
        age = int(age_str)

        if age < 13:
            result = "Child"
            print(Fore.CYAN + "You're not old enough to access this app. Thank you for visiting.")
        elif age < 18:
            result = "Teen"
            print(Fore.BLUE + "Welcome to our server, you have met the age range criteria.")
        else:
            result = "Adult"
            print(Fore.GREEN + "It's never too late to learn new things, right?")
        
        # Save data to the list
        user_data.append({
            "name": name,
            "age": age,
            "result": result,
        })

    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a valid number for your age.")

def show_user_data():
    if not user_data:
        print(Fore.RED + "No data has been saved yet.") # Improved message clarity
    else:
        print(Fore.CYAN + "\n=== Your Saved Data ===") # Changed title for clarity
        for i, data in enumerate(user_data, 1):
            # FIXED: Correct dictionary access using data['key']
            print(Fore.GREEN + f"{i}. Name: {data['name']}, Age: {data['age']}, Category: {data['result']}")

def check_even_odd():
    try:
        number_str = input(Fore.YELLOW + "Enter a number: " + Style.RESET_ALL)
        number = int(number_str)
        if number % 2 == 0:
            print(Fore.GREEN + f"{number} is an even number.")
        else:
            print(Fore.MAGENTA + f"{number} is an odd number.")
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter an integer.")

def calculator():
    print(Style.BRIGHT + Fore.CYAN + "\n--- Simple Calculator ---")
    print(Fore.YELLOW + "1. Addition")
    print(Fore.YELLOW + "2. Subtraction")
    print(Fore.YELLOW + "3. Multiplication")
    print(Fore.YELLOW + "4. Division")

    operation = input(Fore.CYAN + "Select Operation (1/2/3/4): " + Style.RESET_ALL)

    try:
        a = float(input(Fore.YELLOW + "Please enter the first number: " + Style.RESET_ALL))
        b = float(input(Fore.YELLOW + "Please enter the second number: " + Style.RESET_ALL))

        if operation == "1":
            print(Fore.GREEN + f"Result: {a + b}")
        elif operation == "2":
            print(Fore.GREEN + f"Result: {a - b}")
        elif operation == "3":
            print(Fore.GREEN + f"Result: {a * b}")
        elif operation == "4":
            if b != 0:
                print(Fore.GREEN + f"Result: {a / b}")
            else:
                print(Fore.RED + "Error: Cannot divide by zero.")
        else:
            print(Fore.RED + "Invalid operation. Please select 1, 2, 3, or 4.")
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter valid numbers.")

def exit_program():
    print(Fore.BLUE + "Thanks for using this program!")
    sys.exit()

# Main Interactive Menu
# user_data = [] # Moved this line to be initialized at the top level
# so it's globally accessible when age_checking is defined.

while True:
    clear_screen() # Clear screen at the beginning of each loop iteration
    print(Fore.CYAN + f"\n=== Main Menu - Welcome, {name}! ===") # Corrected "Wecome" to "Welcome"
    print(Fore.MAGENTA + "1. Check Age Category")
    print(Fore.MAGENTA + "2. Check Even/Odd Number")
    print(Fore.MAGENTA + "3. Calculator")
    print(Fore.MAGENTA + "4. Show saved data")
    print(Fore.RED + "5. Exit") # Removed space before Exit for consistency

    # FIXED: Updated the prompt to include option 5
    choice = input(Fore.CYAN + "Select Menu (1/2/3/4/5): " + Style.RESET_ALL)

    if choice == "1":
        age_checking(name)
    elif choice == "2":
        check_even_odd()
    elif choice == "3":
        calculator()
    elif choice == "4":
        show_user_data()
    elif choice == "5":
        exit_program()
    else:
        print(Fore.RED + "Invalid choice. Please try again.")

    # FIXED: Included option 4 in the pause list
    if choice in ["1", "2", "3", "4"]:
        print(Fore.BLUE + "\nPress Enter to return to menu...")
        input()