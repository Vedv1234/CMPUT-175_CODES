# Author: Ved Vyas
# Co-Author / Exercise provided by: University of Alberta CMPUT 175 Course Team & Instructors (2023)
# Functionality of code: This file contains my implementation of two different queue data structures:
# BoundedQueue and CircularQueue. The BoundedQueue uses a simple list-based approach, while the 
# CircularQueue uses a more efficient circular buffer implementation. I'm using these to understand 
# different queue implementations and their performance characteristics.

class BoundedQueue:
    def __init__(self, size):
        '''
        Setting up my bounded queue with a maximum size
        '''
        self.__items = []          # I'm using a list to store my queue items
        self.__capacity = size     # Maximum number of items I can store
        
    def enqueue(self, item):
        '''
        My method to add items to the back of the queue
        '''
        # I only add if there's space available
        if len(self.__items) < self.__capacity:
            self.__items.append(item)
        else:
            raise Exception('Error: Queue is full')
    
    def dequeue(self):
        '''
        My method to remove and return items from the front of the queue
        '''
        # Check if I have items to remove
        if not self.isEmpty():
            return self.__items.pop(0)  # Remove and return the first item
        else:
            raise Exception('Error: Queue is empty')
    
    def isEmpty(self):
        '''
        Checking if my queue has any items
        '''
        return len(self.__items) == 0
    
    def isFull(self):
        '''
        Checking if my queue is at maximum capacity
        '''
        return len(self.__items) == self.__capacity
    
    def size(self):
        '''
        Returns how many items are currently in my queue
        '''
        return len(self.__items)
    
    def capacity(self):
        '''
        Returns the maximum size of my queue
        '''
        return self.__capacity
    
    def __str__(self):
        '''
        Creating a nice string representation of my queue
        '''
        return str(self.__items)
    
    def __repr__(self):
        '''
        Detailed representation for debugging
        '''
        return f"BoundedQueue(size={self.__capacity})"

class CircularQueue:
    def __init__(self, size):
        '''
        Setting up my circular queue with a fixed size array
        '''
        self.__capacity = size          # Maximum size of my queue
        self.__items = [None] * size    # Pre-allocating my array
        self.__head = 0                 # Front of my queue
        self.__tail = 0                 # Back of my queue
        self.__count = 0                # Number of items currently in queue
    
    def enqueue(self, item):
        '''
        Adding items to my circular queue
        '''
        if not self.isFull():
            # Using modulo to wrap around to the start if needed
            self.__items[self.__tail] = item
            self.__tail = (self.__tail + 1) % self.__capacity
            self.__count += 1
        else:
            raise Exception('Error: Queue is full')
    
    def dequeue(self):
        '''
        Removing items from my circular queue
        '''
        if not self.isEmpty():
            # Getting the item at the head
            item = self.__items[self.__head]
            # Moving head pointer using circular arithmetic
            self.__head = (self.__head + 1) % self.__capacity
            self.__count -= 1
            return item
        else:
            raise Exception('Error: Queue is empty')
    
    def isEmpty(self):
        '''
        Checking if my circular queue is empty
        '''
        return self.__count == 0
    
    def isFull(self):
        '''
        Checking if my circular queue is full
        '''
        return self.__count == self.__capacity
    
    def size(self):
        '''
        Current number of items in my queue
        '''
        return self.__count
    
    def capacity(self):
        '''
        Maximum capacity of my queue
        '''
        return self.__capacity
    
    def __str__(self):
        '''
        Creating a string representation of my queue
        '''
        # I need to handle the wrap-around case carefully
        if self.isEmpty():
            return "[]"
            
        items = []
        pos = self.__head
        for _ in range(self.__count):
            items.append(str(self.__items[pos]))
            pos = (pos + 1) % self.__capacity
        return "[" + ", ".join(items) + "]"
    
    def __repr__(self):
        '''
        Detailed representation for debugging
        '''
        return f"CircularQueue(size={self.__capacity})"

def main():
    '''
    My test function to make sure everything works correctly
    '''
    # Testing my bounded queue
    print("Testing my Bounded Queue implementation:")
    bq = BoundedQueue(3)
    print("Initial queue:", bq)
    print("Is empty?", bq.isEmpty())
    
    # Testing enqueue
    print("\nTesting enqueue operations:")
    try:
        bq.enqueue("apple")
        bq.enqueue("banana")
        bq.enqueue("orange")
        print("Queue after adding three items:", bq)
        print("Is full?", bq.isFull())
        
        print("\nTrying to add to full queue...")
        bq.enqueue("grape")  # Should raise exception
    except Exception as e:
        print("Got expected error:", e)
    
    # Testing dequeue
    print("\nTesting dequeue operations:")
    print("Removed:", bq.dequeue())
    print("Queue after removal:", bq)
    
    # Testing circular queue
    print("\nTesting my Circular Queue implementation:")
    cq = CircularQueue(3)
    print("Initial circular queue:", cq)
    
    # Adding items to circular queue
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    print("Filled circular queue:", cq)
    
    # Testing circular behavior
    print("\nTesting circular behavior:")
    print("Removed:", cq.dequeue())
    cq.enqueue(4)
    print("After one remove and add:", cq)

if __name__ == '__main__':
    main()