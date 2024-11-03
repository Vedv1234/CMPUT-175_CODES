#----------------------------------------------------
# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 175 Course Team & Instructors (2023) 
# Functionality of code: This is my implementation of a Numerical Tic Tac Toe game 
# where instead of X's and O's, player 1 uses odd numbers (1-9) and player 2 uses 
# even numbers (2-8). The goal is to make a line that sums to 15. I've built this 
# to handle all the game logic, player inputs, and board management.
#----------------------------------------------------

from lab3_NumTicTacToe import NumTicTacToe

def getEntry(player, entries):
    '''
    # I created this function to handle getting valid number inputs from players.
    # It makes sure player 1 only enters odd numbers and player 2 only enters even numbers.
    '''
    # I'm checking which player's turn it is to set their number range
    if player % 2 == 0:
        numDescription = 'even'
        lowerRange = 2
        upperRange = 8        
    else:
        numDescription = 'odd'
        lowerRange = 1
        upperRange = 9         
    
    # I'm formatting my prompt to tell the player what numbers they can use
    prompt = 'Player {}, please enter an {} number ({}-{}): '
    prompt = prompt.format(player, numDescription, lowerRange, upperRange)
    entry = input(prompt)
    return int(entry)

def getCoord(player, dimension):
    '''
    # I wrote this to get the row or column position from players.
    # It helps me keep track of where they want to place their numbers.
    '''
    # I'm setting the valid range for my 3x3 board
    LOWER = 0
    UPPER = 2
    # I'm asking the player to enter either a row or column number
    index = input('Player ' + str(player) + ', please enter a ' + dimension + ': ')
    return int(index)

def isGameOver(myBoard, player):
    '''
    # This is my game-ending checker. It tells me if someone won or if we've got a tie.
    '''
    # I'm checking if the current player just won
    if myBoard.isWinner():
        myBoard.drawBoard()
        print('Player', player, "wins. Congrats!")           
        return True
    # Or if we've filled up the board with no winner
    elif myBoard.boardFull():
        myBoard.drawBoard()
        print("It's a tie.")             
        return True  
    return False

def playAgain():
    '''
    # I use this to ask players if they want another round after the game ends.
    '''
    playAgain = ' ' 
    # I'm making sure I get a valid Y or N answer
    while playAgain[0].upper() not in ['Y', 'N']:
        playAgain = input("Do you want to play another game? (Y/N) ")
    return playAgain[0].upper() == "Y"   

def main():
    '''
    # This is my main game controller. It runs everything and keeps the game flowing.
    '''
    newGame = True
    while newGame:
        # I'm printing a nice title to start each game
        TITLE = "Starting new Numerical Tic Tac Toe game"
        print("-"*len(TITLE))
        print(TITLE)
        print("-"*len(TITLE))
        
        # I'm setting up my fresh game board
        myBoard = NumTicTacToe()
        gameOver = False
        turn = 0
        entries = []
        
        # This is my main game loop
        while not gameOver:
            myBoard.drawBoard()
            
            # I'm getting all the move info from the current player
            entry = getEntry(turn+1, entries)
            row = getCoord(turn+1, 'row')
            col = getCoord(turn+1, 'column')
                                   
            # I'm trying to make the move and checking if the game continues
            if myBoard.update(row, col, entry):
                entries.append(entry)
                gameOver = isGameOver(myBoard, turn+1)
                turn = (turn+1) % 2                
            # If the move wasn't valid, I let them know
            else:
                print('Error: could not make move!')
                
        # After the game ends, I check if they want to play again
        newGame = playAgain()
            
    print('Thanks for playing! Goodbye.')
            
if __name__ == '__main__':
    main()