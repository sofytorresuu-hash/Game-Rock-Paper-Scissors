# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 21:50:43 2026

@author: sofyt
"""

# Unit 4: Functional Programming - Modular Logic

def get_option_name(key_number, data_dict):
    """Returns the string value from the dictionary based on the key."""
    return data_dict.get(key_number, "Unknown")

def determine_winner(user, system):
    """Evaluates relational and logical operators to find the winner."""
    if user == system:
        return "It's a Draw!"
    
    # Logic Rules: 1 beats 3, 2 beats 1, 3 beats 2
    if (user == 1 and system == 3) or \
       (user == 2 and system == 1) or \
       (user == 3 and system == 2):
        return "Congratulations! You Win!"
    else:
        return "The System Wins. Try again!"
    