# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 21:49:36 2026

@author: sofyt
"""

import random
# Import logic from the second file
from game_logic import determine_winner, get_option_name

# Unit 1: Main Instructions
WELCOME_MESSAGE = "Welcome to Rock, Paper, Scissors! 1: Rock, 2: Paper, 3: Scissors."
print(WELCOME_MESSAGE)

# Unit 2: Data Input and Variables
surname = input("Write your surname: ")
print(f"Hello {surname}! Let's begin!")

# Unit 4: Data Structures (Dictionary for mapping)
options = {1: "Rock", 2: "Paper", 3: "Scissors"}

# Unit 3: Repetitive Structure (Game Loop)
continue_playing = "yes"
while continue_playing.lower() == "yes":
    
    # User Input Management
    try:
        user_choice = int(input("Your choice (1, 2 or 3): "))
        if user_choice not in options:
            print("Invalid choice! Please select 1, 2, or 3.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    # System random generation
    system_choice = random.randint(1, 3)
    
    print(f"You chose: {get_option_name(user_choice, options)}")
    print(f"System chose: {get_option_name(system_choice, options)}")

    # Unit 3 & 4: Decision Structure via Function Call
    result = determine_winner(user_choice, system_choice)
    print(f"RESULT: {result}")
    
    continue_playing = input("Do you want to play again? (yes/no): ")

print("Thanks for playing! Memory cleared.")