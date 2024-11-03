# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 175 Course Team & Instructors (2023) 
# Functionality of code: 
# In this lab, I've created a Caesar cipher decryption program. The cool thing about 
# this code is that it takes an encrypted message from a text file and decrypts it 
# using a cipher key that's also in the file. I made sure to handle both uppercase 
# and lowercase letters, and I kept any non-letter characters (like spaces and 
# punctuation) exactly as they are in the original message.

import os  # I'm importing the os module to help me check if files exist on my system

def getInputFile():
    """
    My GetInputFile function asks the user for the name of a text file with a ".txt" extension and then it validates the file name and returns it as a string.

    Returns:
    str which is The valid name of the text file.
    """
    
    # I'm using a while loop here because I want to keep asking for the filename
    # until the user gives me a valid one. This way, my program won't crash if
    # they make a mistake
    while True:
        # I'm using strip() to remove any accidental spaces the user might add
        filename = input("Enter the input filename: ").strip()
        
        # Here I check two things: if the file ends with .txt and if it actually exists
        # I use lower() to make sure it works whether they type .TXT or .txt
        if filename.lower().endswith(".txt") and os.path.exists(filename):
            return filename
        else:
            # If something's wrong with the filename, I give them a helpful error message
            print("Invalid filename or file does not exist. Please re-enter the input filename.")

def decrypt(filename):
    """
    My Decrypt function decrypts a message encoded with a Caesar cipher and prints the decrypted message.

    Parameters:
    This function is taking the filename as a parameter which is of string form: The name of the text file containing the cipher key and encrypted message.

    Returns: Nothing (None)
    """
    
    # I'm using a with statement here because it's the safest way to handle files
    # It automatically closes the file when I'm done, even if there's an error
    with open(filename, 'r') as file:
        # The first line of my file has the cipher key - I need to convert it to an integer
        cipher_key = int(file.readline().strip())
        # The second line has my encrypted message
        encrypted_message = file.readline().strip()

    # I'll store my decrypted message here as I build it character by character
    decrypted_message = ""

    # Now I loop through each character in the encrypted message to decrypt it
    for char in encrypted_message:
        # First, I check if it's a letter - I only want to decrypt letters
        if char.isalpha():
            # I need to know if it's uppercase or lowercase to maintain the case
            is_upper = char.isupper()
            
            # This is where the magic happens - my decryption formula
            # I'm using ord() to convert letters to numbers I can work with
            # Then I apply the Caesar cipher shift and convert back to a letter
            decrypted_char = chr((ord(char) - cipher_key - ord('A' if is_upper else 'a') + 26) % 26 
                                + ord('A' if is_upper else 'a'))
            
            # Add my newly decrypted character to the message
            decrypted_message += decrypted_char
        else:
            # If it's not a letter (like a space or comma), I keep it as is
            decrypted_message += char

    # Finally, I print out my decrypted message
    print("The decrypted message is:")
    # I convert it all to lowercase as required
    print(decrypted_message.lower())

def main():
    # I'm displaying the help documentation for my functions
    help(getInputFile)
    help(decrypt)
    
    # Here's where I actually run my program:
    # First get the filename, then decrypt the message
    filename = getInputFile()
    decrypt(filename)

# This is the standard way to run my program
if __name__ == "__main__":
    main()