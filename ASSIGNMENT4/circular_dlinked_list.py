class Node: #represents a node in a doubly linked lsit, each node has the data, necxt and prev representing the datam nect nidode and previous  node
    def __init__(self, data=None): #I deafult data to None
        self.data = data #the data
        self.next = None #intially pointing to None
        self.prev = None

class CircularDoublyLinkedList: #represnting a circular doubly linke dloist which the carousel will tually be an instance of
    def __init__(self):
        self.head = None #all pointingot none initallt
        self.tail = None
        self.current = None
        self.size = 0 #intially siz eis 0
        self.nodes = []  # This is a list thagt wikl store the nides

    def add_node(self, data):
        new_node = Node(data) #creating a new node by creating an instance of the class ndoe
        if self.size == 0: #if the size of th edoubly linke dlist is 0 , its empty
            self.head = new_node #pointing the head to the new node
            self.tail = new_node #pointing the tail indicating the end of the list is laso the only nod e in the list
            self.current = new_node  # Updating the current to tbe th enerw node
            new_node.next = new_node  #the nex t of the new node is thwe new sonode too, i AM UING THE IDEA of self pointing of the ndoes
            new_node.prev = new_node #the previous of the new node is also the new_node
        else:
            new_node.next = self.current #setting thje next of thhe new node to the node next to the current node in the lsit
            new_node.prev = self.current #setting the prev of the new nde to the ndoe to the current ndoe int he lsit
            self.current.next.prev = new_node.next #updating th enext and prev atteributes of the nodes neighboring the current node to include the new node in the linked list
            self.current.next = new_node #next of the curent node is rhe nex trnode
            self.tail = new_node #tail is also the new nde
        self.size += 1 #incremenrint the size
    

        def display_carousel(carousel): #just a repertion of what is in the carousel.py, coonnecting the doublylinkedlist mclass and carousel
            if carousel.size == 0:
                print("Empty carousel.")
            else:
                current_node = carousel.current
                while True:
                    print(current_node.data['symbol'], end=' ')
                    if current_node == carousel.tail:
                        break
                    current_node = current_node.next


    def remove_current_node(self):
            if self.size == 0: #if size is 0
                raise Exception("Cannot remove node. Carousel is empty.") #raising exception
            elif self.size == 1:
                self.head = None #if only 1 node, the whole linked lis tbecome sempty in whoich case everything points to None again
                self.tail = None
                self.current = None
            else:
                self.current.prev.next = self.current.next #updating th enext of the node preceding th ecureent node to skip over the current node
                self.current.next.prev = self.current.prev #updating th eprev of the node follwoing the current node to point back to the node before the current node effectively remocing th ecurrent node from te dequence
                self.current = self.current.prev  # udpdate current node after removal moving th ecurrent node to the rpreviosus node
                if self.current == self.head: #checking ig the current node is now the head node
                    self.head = self.current.next  # if removing the head node, update head to point to the next node ofte rth eremoved data
                if self.current == self.tail:
                    self.tail = self.current.prev  # if i am removing the tail node, I update the tail attribute to point to the previous node before the removed node
            self.size -= 1  #decrement the size       

    def go_left(self): #raising exeptions for the functionalities that can't be performed if the doubly linked list empty
        if self.size == 0: 
            raise Exception("Cannot move left. Carousel is empty.")
        self.current = self.current.prev

    def go_right(self):
        if self.size == 0:
            raise Exception("Cannot move right. Carousel is empty.")
        self.current = self.current.next

    def display_info(self):
        if self.size == 0:
            raise Exception("No nodes to display information.")
        print(f"Name: {self.current.data['name']}") #prin  these if the expetions are not weaised
        print(f"Symbol: {self.current.data['symbol']}")
        print(f"Class: {self.current.data['class']}")
    def __str__(self):
            return self.data['symbol'] #return the symbol in tring form
