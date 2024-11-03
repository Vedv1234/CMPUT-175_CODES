#----------------------------------------------------
# Author: Ved Vyas
# Co-Author / Exercise provided by: University of Alberta CMPUT 175 Course Team & Instructors (2023)
# Functionality of code: This is my implementation of a web browser simulator that I created for Lab 4. 
# The program simulates basic browser navigation features like entering URLs, going back and forward 
# through browsing history, and quitting the browser. I made it to understand how web browsers handle 
# navigation history and user interactions. It was a great exercise to learn about list manipulation 
# and user input handling in Python.
#----------------------------------------------------

def getAction():
    '''
    Prompts the user to enter a valid action (=, <, >, or q).
    If an invalid action is entered, displays an error message and re-prompts.
    
    Inputs: None
    Returns: str
    '''
    # I'm using an infinite loop here because I want the browser to keep running until the user decides to quit
    while True:
        # I prompt the user with clear instructions about what each symbol means
        action = input("Enter = to enter a URL, < to go back, > to go forward, q to quit: ")
        # I check if the user's input is one of the valid actions I defined
        if action in {'=', '<', '>', 'q'}:
            # If it's valid, I return it to be processed
            return action
        else:
            # If they enter something invalid, I let them know and the loop continues
            print("Invalid entry.")

def goToNewSite(current, pages):
    '''
    Prompts the user to enter a new website address, adds it to my pages list,
    and returns the index to the current site.
    
    Inputs: int, list
    Returns: int
    '''
    # I get the new URL from the user
    new_url = input("URL: ")
    # I add the new URL to my list of pages
    pages.append(new_url)
    # I return the index of the new page, which is the last position in my list
    return len(pages) - 1

def goBack(current, pages):
    '''
    Returns the index of the previous webpage if available, otherwise displays an error
    message and returns the index of the current site.
    
    Inputs: int, list
    Returns: int
    '''
    # I check if there's a previous page to go back to
    if current > 0:
        # If there is, I return the previous index
        return current - 1
    else:
        # If we're at the start, I let the user know they can't go back further
        print("Cannot go back.")
        # I keep them on the current page
        return current

def goForward(current, pages):
    '''
    Returns the index of the next webpage if available, otherwise displays an error
    message and returns the index of the current site.
    
    Inputs: int, list
    Returns: int
    '''
    # I check if there's a next page to go forward to
    if current < len(pages) - 1:
        # If there is, I return the next index
        return current + 1
    else:
        # If we're at the newest page, I let the user know they can't go forward
        print("Cannot go forward.")
        # I keep them on the current page
        return current

def main():
    '''
    Controls the main flow of my web browser simulator.
    
    Inputs: None
    Returns: None
    '''
    # I set my homepage to the UAlberta CS department website
    HOME = 'www.cs.ualberta.ca'
    # I create my initial history list with just the homepage
    websites = [HOME]
    # I set my starting position to the first (and only) page
    currentIndex = 0
    # I initialize my quit flag to False so the browser stays running
    quit = False
    
    # My main browser loop - keeps running until the user wants to quit
    while not quit:
        # I show the user which website they're currently on
        print('\nCurrently viewing', websites[currentIndex])
        # I get their next action choice
        action = getAction()
        
        # I process their choice
        if action == '=':
            # They want to enter a new URL, so I call my new site function
            currentIndex = goToNewSite(currentIndex, websites)
        elif action == '<':
            # They want to go back, so I call my back function
            currentIndex = goBack(currentIndex, websites)
        elif action == '>':
            # They want to go forward, so I call my forward function
            currentIndex = goForward(currentIndex, websites)
        elif action == 'q':
            # They want to quit, so I set my quit flag to True
            quit = True
    
    # I show a nice goodbye message when they're done
    print('Browser closing...goodbye.')

        
if __name__ == "__main__":
    main()