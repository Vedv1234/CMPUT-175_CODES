import json #importing the json module
import os 
#need the os module for clearign the screen
import time #I will need time.sleep for delay
import art #my art py file
from circular_dlinked_list import CircularDoublyLinkedList #importing curcular doubly linked lsit

# My funciton here is opening th erjson file by opening file for r , I was having troubleextractign the emoji from the file but whenI used encoding utf8 , it was much easeir, good learning experienc there
def read_json_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        emojis_data = json.load(file) #loading the file to ge temojis data
    return emojis_data #returnignthe emojis_data which is a dictionarry converted from the json string

# My function to take user input, strippingot remove trailing and leading whitespaces
def take_user_input(prompt):
    return input(prompt).strip()
# Function to find the object to be added to the Circular Doubly Linked List
def find_object_to_add(emojis_data, search_word):  #taking the oarsed json data and a searchcd worda s input
    search_word = search_word.lower() #coverting the search word to lowercase using the lower method
    for category in emojis_data: #for every category class like animals int he emojis_Data dicitonary,I am searching for an emoji whose namematches the search word.When a matchign emoji is ofound, it name , its sumbol and its class is returned as a dicitionary
        for emoji_name, emoji_symbol in category['emojis'].items():
            if search_word in emoji_name.lower(): 
                return {'name': emoji_name, 'symbol': emoji_symbol, 'class': category['class']}
    return None

def display_carousel(carousel):
    if carousel.size == 0: #cheecking if the dize od the carousel is 0, indicating that there are no node sin the carousel, if this conditionis true,it prints empty carousel
        print("Empty carousel.")
    else:  #if niot empty
        current_node = carousel.current #the node currrently selceted in the carousel is the center of the display
        while True:
            time.sleep(1) #the delay
            print(current_node.data['symbol'], end=' ')#printing the current node and using the end=' ' paramter to avoin printing a newline character faafter each symbol which would cause them to be preinte donseparate lines
            if current_node == carousel.tail: #if the curent node is the same s the tail of the caroselm it means I ahve traversed the entire carosel so I exit the loop using break, Illegal but i had no other optionunforntutelt
                break
            current_node = current_node.next #udating the current node to be the next node int he carousel effectivelt moving to the next node in the traversal



def main():
    carousel = CircularDoublyLinkedList() #create an instance of the carousel class
    emojis_data = read_json_file('emojis.json') #reading the emoji data, calling my function

    while True: #starting an  infinite loop
        if carousel.size >= 2: #checking if the siz eof the carousel if hreater than 2, if there are arleast 2 emoji frames, it means that I have enough emoji frames to display options ofr adding, deleting , moving left,moving right, gettigninformation and quitting the program
            print("\nOptions:") #printign the optuons
            print("ADD: Add an emoji frame")
            print("DEL: Delete current emoji frame")
            print("INFO: Retrieve info about current frame")
            print("L: Move left")
            print("R: Move right")
            print("QUIT: Quit the program")
        elif carousel.size == 1: #if the size is 1, limited optiosn
            print("\nOptions:")
            print("ADD: Add an emoji frame")
            print("QUIT: Quit the program")
        else:
            print("\nType any of the following commands to perform the action:")
            print("ADD: Add an emoji frame")
            print("QUIT: Quit the program")

        choice = take_user_input("Enter your choice: ").upper()#askignthe user to select which option of functionality they want

        if choice == "ADD": #if hey want o add
            if carousel.size == 0: #if no elements initally then
                search_word = input("Enter the name of the emoji you want to add: ").strip() #askign user's emoji inpout
                emoji = find_object_to_add(emojis_data, search_word) #calling the find object in the enojis_data
                if emoji:#if emoji is found
                    carousel.add_node(emoji) #add the node to the carousel soubly linked list
                    time.sleep(1)#delay
                    print(art.info_display) #print the info display of art
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear') #I learnt about this function from pandasdf, you can use the os module clear screen tempparily and then display the updated carousel
                    print(art.one_node_carousel.format(emoji['symbol'], emoji['symbol'])) #printign the one node carousel deifninged in th eart module, using the string format method to replace the place holders {} in the art template with the symbols of the emoji.Using 2 same parameter s because I was facing major issues when i had only 1 placeholdr in the template, somehow by addign 2 it worked and 2 symobls were not being displayed in one frame so I LEFT THE CODE THIS WAY NOT TO CAUSE ANY ERRORS
                else:
                    print("Emoji not found. Try again.") #if emoji is not found
            elif carousel.size == 1: #there esists one node already
                print("What do you want to add?") 
                add_choice = input("(Enter the name of the emoji): ").strip()
                new_emoji = find_object_to_add(emojis_data, add_choice)
                if new_emoji:
                    print("On which side do you want to add the emoji frame? (left/right): ")
                    side_choice = input("(left/right): ").strip().upper() #asking whther emoji wants to added to the left or right of current emoji frame
                    if side_choice == "LEFT": #if ledt
                        carousel.add_node(new_emoji) #add the ndoe left
                        time.sleep(1) #delay
                        print(art.adding_left)#aniamtion of adding left
                        
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')   #clear screen                      
                        print(art.frame_carousel.format(carousel.current.prev.data['symbol'], 
                                                             new_emoji['symbol'], 
                                                             carousel.current.prev.data['symbol'])) #formatting the framecarousel, the first parameter is accessign the  symbol of the emoji stored in the node before the current node  It is used to represent the emoji symbol on the left side of the current emoji being added.The secind parameter is also accessing the symbol, the duplication asllwoed to keep a key error away so I went with it.
                    elif side_choice == "RIGHT": #same as left but opposite
                        carousel.add_node(new_emoji)
                        time.sleep(1)
                        print(art.adding_right)
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')                        
                        print(art.two_nodes_carousel.format(carousel.current.prev.data['symbol'], 
                                                             carousel.current.data['symbol'], 
                                                             new_emoji['symbol']))
                    else:
                        print("Invalid choice. Please try again.") #not left or right inputted by usetr
                else:
                    print("Emoji not found. Try again.")# emoji not found
            elif carousel.size >= 2: #if the size is hreater than 2 curentl
                print("What do you want to add?")
                add_choice = input("(Enter the name of the emoji): ").strip()
                new_emoji = find_object_to_add(emojis_data, add_choice)
                if new_emoji:
                    print("On which side do you want to add the emoji frame? (left/right): ") #same proceure
                    side_choice = input("(left/right): ").strip().upper()
                    if side_choice == "LEFT":
                        carousel.go_left() # but first we got left of the nkde
                        carousel.add_node(new_emoji) #and then create the new nide
                        time.sleep(1)
                        print(art.adding_left)
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')                        
                        print(art.frame_carousel.format(carousel.current.prev.prev.data['symbol'],
                                                               carousel.current.prev.data['symbol'], 
                                                               new_emoji['symbol'], 
                                                               carousel.current.prev.data['symbol'], 
                                                               carousel.current.prev.prev.data['symbol']))
                    elif side_choice == "RIGHT":
                        carousel.add_node(new_emoji)
                        carousel.go_right()  #or for the right , go right of the current ndoe and the create the new ndoe
                        time.sleep(1)
                    
                        print(art.adding_right)
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')                        
                        print(art.frame_carousel.format(carousel.current.prev.prev.data['symbol'], 
                                                               carousel.current.prev.data['symbol'], 
                                                               new_emoji['symbol'], 
                                                               carousel.current.prev.data['symbol'], 
                                                               carousel.current.prev.prev.data['symbol'])) #printing th eprevo fo the data
                    else:
                        print("Invalid choice. Please try again.")
                else:
                    print("Emoji not found. Try again.")

        elif choice == "L":
            carousel.go_left() #mving the current position one step to the left,then updating th ecurrent pinter to the previosu node in the linked list
            time.sleep(1)
            print(art.left_movement) #printing th evisual representation of the left movmeemnt message,for hthe art file
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')#celaring th escreen
            print(art.frame_carousel.format(carousel.current.prev.prev.data['symbol'],
                                                   carousel.current.prev.data['symbol'], 
                                                   carousel.current.data['symbol'], 
                                                   carousel.current.next.data['symbol'], 
                                                   carousel.current.next.next.data['symbol'])) # subsitiutiong the placeholder swith the subol of the emoji one step before the current node displyed on the left side of the current emoji, dulicated to avoid tj==he key error I was faicng

        elif choice == "R": #same as left
            carousel.go_right()
            time.sleep(1)
            print(art.right_movement)
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')               
            
            print(art.frame_carousel.format(carousel.current.prev.prev.data['symbol'],
                                                   carousel.current.prev.data['symbol'], 
                                                   carousel.current.data['symbol'], 
                                                   carousel.current.next.data['symbol'], 
                                                   carousel.current.next.next.data['symbol']))

        elif choice == "DEL": #if the choice is delete
            if carousel.size == 0: #if the carousel is empty, i print a message saying that the carousel is empty
                time.sleep(1)
                print(art.delete_action)
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')               
                                
                print("Cannot delete. Carousel is empty.")
            else:
                carousel.remove_current_node()
                if carousel.size == 0: #this may seem erroneous but this bart of the code will never be executed if previous if statement is executed , also not coding the carousel.size==o if statement agaiwas throwing erros so I just coded it
                    time.sleep(1)
                    print(art.delete_action) #delete action visualtiizon form art.py is preseent here
                    time.sleep(1)                    
                    print("Only node in Carousel has been deleted") #if t=inly 1 node in carousel, then message stating that the only niod ehas been deleted
                elif carousel.size == 1:
                    time.sleep(1)
                    print(art.delete_action)
                    time.sleep(1)                    
                    print("Only node in Carousel has been deleted")  
                elif carousel.size == 2:
                    time.sleep(1)
                    print(art.delete_action)
                    time.sleep(1)                    
                    print(art.frame_carousel) #print the empty frame
                elif carousel.size >= 3:
                    time.sleep(1)
                    print(art.delete_action)
                    time.sleep(1)                    
                    print(art.frame_carousel.format(carousel.current.prev.data['symbol'],
                                                           carousel.current.data['symbol'], 
                                                           carousel.current.next.data['symbol'])) #print the empty format witht he remainign emojis 
        elif choice == "INFO":
            if carousel.size == 0: #if no info
                print("No nodes to display information.")
            else:
                carousel.display_info() #cakl th diplau=y info function

        elif choice == "QUIT":
            print("Quitting the program.") #qutting th eprogram
            break

        else:
            print("Invalid choice. Please try again.")  #no vlaid choice

main()

