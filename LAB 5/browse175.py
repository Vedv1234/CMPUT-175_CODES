#----------------------------------------------------
# Author: Ved Vyas
# Co-Author / Exercise provided by: University of Alberta CMPUT 175 Course Team & Instructors (2023)
# Functionality of code: This is my enhanced version of the browser simulator with a terminal-based UI.
# I've added some cool ANSI terminal features to make it look more like a real browser with buttons
# and navigation hints. It's pretty neat how it displays everything in color and proper positioning!
#----------------------------------------------------

import os
from time import sleep
import stack

# I need this for Windows terminals to show ANSI colors
os.system("")

def print_location(x, y, text):
    '''
    I'm using this to print text exactly where I want it on the screen
    '''
    print("\033[{1};{0}H{2}".format(x, y, text))

def clear_screen():
    '''
    This helps me keep the display clean
    '''
    # I need to handle both Windows and Unix systems differently
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
def display_error(error):
    '''
    I use this to show error messages in red
    '''
    move_cursor(0, 3)
    print("\033[6;31;40m{:^80}\033[0m".format(error))
    sleep(0.6)
    clear_screen()

def print_header():
    '''
    This prints my cool green browser header
    '''
    print("\033[0;32;40m{:^80}\033[0m".format("[ BROWSE-175 ]"))

def move_cursor(x, y):
    '''
    Helps me position the cursor anywhere on screen
    '''
    print("\033[{1};{0}H".format(x, y), end='')

def display_current_site(current):
    '''
    Shows which site we're currently on
    '''
    print("\033[2;32;40m{:^80}\033[0m".format("Currently viewing: " + current))
    print("\033[4;30;40m{:^80}\033[0m".format(""))

def display_hint(message):
    '''
    Shows navigation help at the bottom
    '''
    print("\033[40;30;47m{:^80}\033[0m".format(message))

def display_buttons(back, fwd):
    '''
    This creates my navigation buttons at the top
    '''
    move_cursor(0, 1)
    
    # I only show the back/forward buttons if we can actually use them
    back_label = "(<) BACK" if not getattr(back, 'is_empty', lambda: not back)() else " " * 7
    fwd_label = "FORWARD (>)" if not getattr(fwd, 'is_empty', lambda: not fwd)() else " " * 67
    
    print("\033[1;32;40m{:<10}{:>70}\033[0m".format(back_label, fwd_label))

def goToNewSite(current, bck, fwd):
    '''
    Handles navigation to a new site
    '''
    new_site = input("URL: ")
    
    # Clear forward history when going to a new site
    fwd.clear()
    
    # Save current site to back stack
    bck.push(current)
    
    # Update current site
    current = new_site
    
    return current

def goBack(current, back, fwd):
    '''
    Handles the back button
    '''    
    if not back.isEmpty():
        fwd.push(current)
        return back.pop()
    else:
        display_error("Cannot go back.")
        return current

def goForward(current, back, fwd):
    '''
    Handles the forward button
    '''    
    if not fwd.is_empty():
        back.push(current)
        return fwd.pop()
    else:
        display_error("Cannot go forward.")
        return current
    
def main():
    # Starting at the CS homepage
    HOME = 'www.cs.ualberta.ca'
    back = stack.Stack()
    fwd = stack.Stack()
    current = HOME
    quit = False

    # Main browser loop
    while not quit:
        clear_screen()
        print_header()
        display_current_site(current)
        display_buttons(back, fwd)

        move_cursor(0, 20)
        display_hint("Use <, > to navigate, = to enter a URL, q to quit")
        print_location(5, 5, "Action: ")
        move_cursor(13, 5)
        action = input()
        
        # Handle user actions
        if action == '=':
            current = goToNewSite(current, back, fwd)
        elif action == '<':
            current = goBack(current, back, fwd)
        elif action == '>':
            current = goForward(current, back, fwd)
        elif action == 'q':
            clear_screen()
            quit = True
        else:
            display_error('Invalid action!')

if __name__ == "__main__":
    main()