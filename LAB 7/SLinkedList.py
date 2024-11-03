"""
Author: Ved Vyas
Co-Author / Exercise provided by: University of Alberta CMPUT 175 Course Team & Instructors (2023)
Functionality of code: In this code, I've implemented a singly-linked list data structure where 
each node points to the next node in the sequence. I've built this with all the essential operations 
like adding elements, removing them, and searching through the list. It's a fundamental data structure 
that I find really useful for managing sequential data where I only need to traverse in one direction.
"""

class SLinkedListNode:
    def __init__(self, initData, initNext):
        # Here I'm creating a new node with its initial data and next pointer
        self.data = initData  # This is where I store the actual data
        self.next = initNext  # This points to the next node in my list

    def getNext(self):
        # I use this to get the reference to the next node
        return self.next

    def getData(self):
        # This helps me get the data stored in my node
        return self.data

    def setData(self, newData):
        # When I need to change the data in my node, I use this
        self.data = newData

    def setNext(self, newNext):
        # I use this to update where my node points to
        self.next = newNext


class SLinkedList:
    def __init__(self):
        # I'm setting up my empty linked list here
        self.head = None  # This marks the start of my list
        self.size = 0  # I'll keep track of how many items are in my list

    def add(self, item):
        # This is how I add something to the start of my list
        new_node = SLinkedListNode(item, None)  # Create my new node
        new_node.setNext(self.head)  # Point it to the current head
        self.head = new_node  # Make it the new head
        self.size += 1  # List got bigger!

    def append(self, item):
        # This helps me add something to the end of my list
        new_node = SLinkedListNode(item, None)  # Create my new node
        current = self.head  # Start at the beginning

        if self.size == 0:
            # If my list is empty, just use add
            self.add(item)
        else:
            # Otherwise, I need to find the end of the list
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(new_node)  # Add my new node at the end
            self.size += 1  # List got bigger!

    def insert(self, pos, item):
        # I use this when I want to put something at a specific position
        assert isinstance(pos, int), "Position must be an integer."
        assert pos >= 0, "Position cannot be negative."

        new_node = SLinkedListNode(item, None)

        if pos == 0:
            # Adding at the start
            new_node.setNext(self.head)
            self.head = new_node
        elif pos == self.size:
            # Adding at the end
            current = self.head
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(new_node)
        elif 0 < pos < self.size:
            # Adding somewhere in the middle
            current = self.head
            for _ in range(pos - 1):
                current = current.getNext()
            new_node.setNext(current.getNext())
            current.setNext(new_node)
        else:
            # Oops, that position doesn't make sense
            raise ValueError("Invalid position for insertion.")

        self.size += 1  # Don't forget to increase the size!

    def remove(self, item):
        # This helps me take something out of my list
        if self.size == 0:
            raise Exception('List is Empty')
        
        current = self.head
        previous = None
        found = False

        # Let's find what we're looking for
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if not found:
            raise Exception('Item not in list')
        else:
            if previous is None:
                # If it's the first item
                self.head = current.getNext()
            else:
                # If it's anywhere else
                previous.setNext(current.getNext())
            self.size -= 1  # List got smaller!

    def index(self, item):
        # I use this to find where something is in my list
        if self.size == 0:
            raise Exception('List is empty')
        
        position = 0
        found = False
        current = self.head

        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                position += 1

        if found:
            return position
        else:
            return 'Item not found'

    def pop(self):
        # This helps me remove and return the last item
        if self.size == 0:
            raise Exception('List is empty')
        
        current = self.head
        previous = None

        # Find the last node
        while current.getNext() is not None:
            previous = current
            current = current.getNext()

        if previous is None:
            # If there's only one item
            self.head = None
        else:
            previous.setNext(None)

        self.size -= 1
        return current.getData()

    def __str__(self):
        # This helps me print my list in a nice format
        current = self.head
        string = ''

        while current is not None:
            string = string + str(current.getData()) + '->'
            current = current.getNext()

        return string

    def getSize(self):
        # This tells me how many items are in my list
        return self.size


def main():
    # Here I'm going to test out all the features of my singly-linked list
    slist = SLinkedList()  # Creating my empty list to play with

    # Let me add some test data
    slist.add(2)  # Adding some numbers and a letter at the start
    slist.add(4)
    slist.add('A')
    slist.append(77)  # And some at the end
    slist.append(6)
    slist.append('Z')

    # I'll print out what I've got so far
    print('Original List:', slist.getSize(), 'elements')  # Showing how many things are in my list
    print(slist)  # Taking a look at the whole list
    print()

    # Let's try inserting some things at different spots
    slist.insert(0, 'start')  # Adding 'start' at the beginning
    print('After inserting the word start at position 0:', slist.getSize(), 'elements')
    print(slist)
    print()

    slist.insert(7, 'end')  # Adding 'end' at the end
    print('After inserting the word end at position 7:', slist.getSize(), 'elements')
    print(slist)
    print()

    slist.insert(4, 'middle')  # Adding 'middle' somewhere in the middle
    print('After inserting middle at position 4:', slist.getSize(), 'elements')
    print(slist)


if __name__ == "__main__":
    main()