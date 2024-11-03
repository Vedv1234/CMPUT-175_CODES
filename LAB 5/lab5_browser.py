#----------------------------------------------------
# Author: Ved Vyas
# Co-Author / Exercise provided by: University of Alberta CMPUT 175 Course Team & Instructors (2023)
# Functionality of code: This is my implementation of a simple web browser simulator. I've built it to understand
# how web browsers handle navigation history. It's pretty cool - it lets you go forward and backward between
# pages just like a real browser. I'm using my stack implementation to keep track of the history.
#----------------------------------------------------

from stack import Stack  # I'm importing my stack implementation that I'll need for navigation

def getAction():
    '''
    I'm using this to get user input for browser navigation
    '''
    # Asking the user what they want to do
    user_input = input("Enter = to enter a URL, < to go back, > to go forward, q to quit: ")
    
    # Making sure they entered something valid
    if user_input not in {'=', '<', '>', 'q'}:
        raise Exception('Invalid entry.')
    
    return user_input

def goToNewSite(current, bck, fwd):
    '''
    This is how I handle when users want to visit a new website
    '''
    # Getting the new URL from the user
    new_site = input("URL: ")
    
    # When going to a new site, I clear the forward history
    # This is how real browsers work too!
    fwd.clear()
    
    # I save the current site to the back stack
    bck.push(current)
    
    # Update where we are now
    current = new_site
    
    return current

def goBack(current, bck, fwd):
    '''
    This handles the back button functionality
    '''
    try:
        # Trying to get the previous site from my back stack
        previous_site = bck.pop()
        
        # I save where we are now to the forward stack
        fwd.push(current)
        
        # Move to the previous site
        current = previous_site
        
    except Exception as e:
        # If there's no history, I let the user know
        print(e.args[0])
    
    return current

def goForward(current, bck, fwd):
    '''
    This handles the forward button functionality
    '''
    try:
        # Getting the next site from my forward stack
        next_site = fwd.pop()
        
        # Save current location to back stack
        bck.push(current)
        
        # Move to the next site
        current = next_site
        
    except Exception as e:
        # Let the user know if there's nowhere to go forward to
        print(e.args[0])
        
    return current

def main():
    '''
    This is where I tie everything together
    '''
    # Starting at the CS department homepage
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    
    current = HOME
    quit = False
    
    # Main browser loop
    while not quit:
        print('\nCurrently viewing', current)
        try:
            action = getAction()
            
            # Handle whatever the user wants to do
            if action == '=':
                current = goToNewSite(current, back, forward)
            elif action == '<':
                current = goBack(current, back, forward)
            elif action == '>':
                current = goForward(current, back, forward)
            elif action == 'q':
                quit = True
            
        except Exception as actionException:
            print(actionException.args[0])
            
    print('Browser closing...goodbye.')    

if __name__ == "__main__":
    main()