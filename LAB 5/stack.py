#----------------------------------------------------
# Author: Ved Vyas
# Co-Author / Exercise provided by: University of Alberta CMPUT 175 Course Team & Instructors (2023)
# Functionality of code: This is my implementation of a Stack data structure that I'm using for my web browser
# simulation. I've created this to handle the back/forward navigation history. It's a pretty neat way to keep
# track of website navigation - kind of like how Chrome or Firefox handles their back/forward buttons.
#----------------------------------------------------

class Stack:
    def __init__(self):
        # I'm starting with an empty list to store my stack elements
        # The back of the list will be my top of the stack
        self.items = []
    
    def push(self, item):
        # I'm adding new items to my stack by appending them to the list
        # This means the newest item will always be at the back
        self.items.append(item)
    
    def pop(self):       
        # Before popping, I need to make sure my stack isn't empty
        if not self.items:
            # If someone tries to pop from an empty stack, I'll let them know that's not possible
            raise Exception("Cannot pop from an empty stack")
        # If we have items, I'll remove and return the last one
        return self.items.pop()
    
    def peek(self):      
        # First checking if there's anything to peek at
        if not self.items:
            # Can't peek at nothing!
            raise Exception("Cannot peek an empty stack")
        # Returning the last item without removing it
        return self.items[len(self.items) - 1]
    
    def isEmpty(self):
        # Simple check to see if my stack has any items
        return not self.items
    
    def size(self):
        # Just returning how many items I've got in my stack
        return len(self.items)
    
    def show(self):
        # This helps me debug by showing what's in my stack
        print(self.items)
    
    def __str__(self):
        # I'm creating a nice string representation of my stack
        stackAsString = ''
        # Going through each item and adding it to my string
        for item in self.items:
            stackAsString += str(item) + ' '
        return stackAsString
    
    def clear(self):
        # When I need to start fresh, this wipes out all items
        self.items = []