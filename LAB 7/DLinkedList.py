"""
Author: Ved Vyas
Co-Author / Exercise provided by: University of Alberta CMPUT 175 Course Team & Instructors (2023)
Functionality of code: In this implementation, I've created a doubly-linked list data structure 
where each node has references to both its next and previous nodes. This makes it really useful 
for applications where I need to traverse the list in both directions. I've included all the 
essential operations like adding, removing, and searching for elements, which gives me a lot of 
flexibility in manipulating the list structure.
"""

class DLinkedListNode:
    def __init__(self, initData, initNext, initPrevious):
        # Here I'm setting up a new node with its initial values
        self.data = initData  # This stores the actual data I want to keep in the node
        self.next = initNext  # This points to the next node in my list
        self.previous = initPrevious  # This points to the previous node in my list

        # I need to make sure the connections are properly set up in both directions
        if initNext is not None:
            self.next.previous = self  # I'm linking the next node back to this one
        if initPrevious is not None:
            self.previous.next = self  # I'm linking the previous node forward to this one

    def getData(self):
        # I use this to get the data stored in my node
        return self.data

    def setData(self, newData):
        # When I need to update the data in my node, I use this
        self.data = newData

    def getNext(self):
        # This helps me get the reference to the next node
        return self.next

    def getPrevious(self):
        # This helps me get the reference to the previous node
        return self.previous

    def setNext(self, newNext):
        # I use this to update the reference to the next node
        self.next = newNext

    def setPrevious(self, newPrevious):
        # I use this to update the reference to the previous node
        self.previous = newPrevious


class DLinkedList:
    def __init__(self):
        # I'm initializing my empty doubly-linked list here
        self.__head = None  # This marks the start of my list
        self.__tail = None  # This marks the end of my list
        self.__size = 0  # I'll keep track of how many items are in my list

    def search(self, item):
        # This helps me find if an item exists in my list
        current = self.__head  # I start at the beginning
        found = False  # Haven't found it yet!

        # I'll keep looking until I either find it or reach the end
        while current is not None and not found:
            if current.getData() == item:
                found = True  # Found it!
            else:
                current = current.getNext()  # Keep looking

        return found

    def index(self, item):
        # I use this to find where in my list an item is located
        current = self.__head
        found = False
        index = 0  # I'll count positions as I go

        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index += 1

        if not found:
            index = -1  # If I didn't find it, I return -1

        return index

    def add(self, item):
        # This is how I add something to the start of my list
        new_node = DLinkedListNode(item, self.__head, None)
        if self.__head is not None:
            self.__head.setPrevious(new_node)  # Link back to new node
        else:
            self.__tail = new_node  # If list was empty, this is also the tail
        self.__head = new_node  # New node becomes the head
        self.__size += 1  # List got bigger!

    def remove(self, item):
        # I use this to take something out of my list
        current = self.__head
        found = False

        # First, I need to find it
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        if found:
            # Now I need to fix the links around the removed node
            if current.getPrevious() is not None:
                current.getPrevious().setNext(current.getNext())
            else:
                self.__head = current.getNext()  # If it was the head, update head

            if current.getNext() is not None:
                current.getNext().setPrevious(current.getPrevious())
            else:
                self.__tail = current.getPrevious()  # If it was the tail, update tail

            self.__size -= 1  # List got smaller
            return

    def append(self, item):
        # This is how I add something to the end of my list
        new_node = DLinkedListNode(item, None, self.__tail)
        if self.__tail is not None:
            self.__tail.setNext(new_node)  # Link forward to new node
        else:
            self.__head = new_node  # If list was empty, this is also the head
        self.__tail = new_node  # New node becomes the tail
        self.__size += 1

    def insert(self, pos, item):
        # I use this when I want to put something at a specific position
        assert isinstance(pos, int), "Position must be an integer."
        assert 0 <= pos <= self.__size, "Invalid position for insertion."

        if pos == 0:
            self.add(item)  # Adding at the start
        elif pos == self.__size:
            self.append(item)  # Adding at the end
        else:
            current = self.__head
            for _ in range(pos - 1):
                current = current.getNext()  # Move to insertion point
            new_node = DLinkedListNode(item, current.getNext(), current)
            current.getNext().setPrevious(new_node)
            current.setNext(new_node)
            self.__size += 1

    def pop1(self):
        # This helps me remove and return the last item
        if self.__size == 0:
            return None  # Can't pop from an empty list!

        item = self.__tail.getData()
        self.__tail = self.__tail.getPrevious()

        if self.__tail is not None:
            self.__tail.setNext(None)
        else:
            self.__head = None  # List is now empty

        self.__size -= 1
        return item

    def pop(self, pos=None):
        # I can use this to remove and return an item from any position
        if self.__size == 0:
            return None

        if pos is None:
            return self.pop1()  # If no position given, pop from the end

        assert isinstance(pos, int), "Position must be an integer."
        assert 0 <= pos < self.__size, "Invalid position for pop."

        current = self.__head
        for _ in range(pos):
            current = current.getNext()

        item = current.getData()

        # Fix the links around the popped node
        if current.getPrevious() is not None:
            current.getPrevious().setNext(current.getNext())
        else:
            self.__head = current.getNext()

        if current.getNext() is not None:
            current.getNext().setPrevious(current.getPrevious())
        else:
            self.__tail = current.getPrevious()

        self.__size -= 1
        return item

    def searchLarger(self, item):
        # This helps me find the first item that's bigger than what I'm looking for
        current = self.__head
        position = 0

        while current is not None:
            if current.getData() > item:
                return position  # Found one!
            else:
                current = current.getNext()
                position += 1

        return -1  # Didn't find anything larger

    def getSize(self):
        # This tells me how many items are in my list
        return self.__size

    def getItem(self, pos):
        # I use this to get an item at a specific position
        assert isinstance(pos, int), "Position must be an integer."

        if pos >= 0:
            current = self.__head
            for _ in range(pos):
                current = current.getNext()
            return current.getData()
        else:
            current = self.__tail
            for _ in range(-pos - 1):
                current = current.getPrevious()
            return current.getData()

    def __str__(self):
        # This helps me print my list in a nice format
        current = self.__head
        elements = []

        while current is not None:
            elements.append(str(current.getData()))
            current = current.getNext()

        return " ".join(elements)

def test():
    # Here I'm testing if my doubly-linked list works correctly
    linked_list = DLinkedList()  # Creating a new empty list
    linked_list.add("World")  # Adding first element
    linked_list.add("Hello")  # Adding second element

    # Making sure everything works as expected
    assert str(linked_list) == "Hello World"
    assert linked_list.getSize() == 2
    assert linked_list.getItem(0) == "Hello"
    assert linked_list.getItem(1) == "World"

    print("Original List:", str(linked_list).strip())
    
    assert linked_list.pop(1) == "World"
    print("List after pop(1):", str(linked_list).strip())

    assert linked_list.pop() == "Hello"
    print("List after pop():", str(linked_list).strip())

    assert linked_list.getSize() == 0  # Should be empty now

test()