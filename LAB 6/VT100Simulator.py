# Author: Ved Vyas
# Co-Author / Exercise provided by: University of Alberta CMPUT 175 Course Team & Instructors (2023)
# Functionality of code: This is my implementation of a VT100 terminal simulator. It allows me to 
# experiment with ANSI escape codes to create colorful terminal output. I use this to better understand 
# how terminal control codes work and how to create interactive terminal interfaces.

import os

# My dictionary of ANSI escape codes for different colors and effects
ANSI = {
    "RED": "\033[31m",        # Text color codes
    "GREEN": "\033[32m",
    "BLUE": "\033[34m",
    "HRED": "\033[41m",       # Background color codes
    "HGREEN": "\033[42m",
    "HBLUE": "\033[44m",
    "UNDERLINE": "\033[4m",   # Text style
    "RESET": "\033[0m",       # Reset all formatting
    "CLEARLINE": "\033[0K"    # Clear line from cursor position
}

def clear_screen():
    '''
    My function to clear the terminal screen cross-platform
    '''
    if os.name == "nt":  # For Windows
        os.system("cls")
    else:  # For Mac/Linux
        os.system("clear")

def move_cursor(x, y):
    '''
    Moves my cursor to a specific position in the terminal
    '''
    print("\033[{};{}H".format(x, y), end="")

def display_title():
    '''
    Shows my title with blue underline effect
    '''
    print(ANSI["UNDERLINE"] + ANSI["BLUE"] + "VT100 SIMULATOR" + ANSI["RESET"])

def get_user_input(prompt, x, y):
    '''
    Gets input from user at a specific screen position
    '''
    move_cursor(x, y)
    user_input = input(prompt).strip().upper()
    return user_input

def apply_style(text_color, bg_color):
    '''
    Applies the chosen color combination to my title
    '''
    title = ANSI[text_color] + ANSI[bg_color] + "VT100 SIMULATOR" + ANSI["RESET"]
    clear_screen()
    display_title()
    print(title)

def main():
    '''
    My main program loop for the VT100 simulator
    '''
    # Enable ANSI escape codes in Windows terminal
    os.system("")  
    
    # Setting up my initial screen
    clear_screen()
    display_title()
    
    while True:
        # Getting text color choice from user
        text_color = get_user_input("Enter a text colour: ", 3, 21)
        if text_color == "EXIT":
            break
        
        # Getting background color choice
        bg_color = get_user_input("Enter a background colour: ", 4, 21)
        if bg_color == "EXIT":
            break
        
        # Checking if user input is valid and applying colors
        if text_color in {"RED", "GREEN", "BLUE"} and bg_color in {"RED", "GREEN", "BLUE", "NONE"}:
            # If background isn't 'NONE', I add 'H' prefix for highlight colors
            apply_style(text_color, "H" + bg_color if bg_color != "NONE" else "")
        else:
            # Clearing invalid input and resetting cursor position
            move_cursor(3, 21)
            print(ANSI["CLEARLINE"])
            move_cursor(3, 21)

if __name__ == "__main__":
    main()