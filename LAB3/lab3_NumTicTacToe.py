#----------------------------------------------------
# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 175 Course Team & Instructors (2023) 
# Functionality of code: This is my implementation of the Numerical Tic Tac Toe board class.
# I've built all the core game mechanics here - from creating the board to checking for winners.
# The unique thing about my version is that it uses numbers instead of X's and O's, where
# players need to create lines that sum to 15 to win.
#----------------------------------------------------

class NumTicTacToe:
    def __init__(self):
        # I'm creating my game board as a 3x3 grid filled with zeros
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        # I'm setting the board size - might make it configurable in the future
        self.size = 3

    def drawBoard(self):
        # I'm starting with a space to align my column numbers nicely
        print(" ", end="")
        # I'm printing the column numbers across the top
        for i in range(self.size):
            print(f" {i}", end="")
        print()
        
        # Now I'm drawing each row of my board
        for i in range(self.size):
            # First I print the row number
            print(i, end=" ")
            # Then I go through each cell in this row
            for j in range(self.size):
                # If the cell is empty (0), I show a vertical bar
                if self.board[i][j] == 0:
                    print("|", end=" ")
                # Otherwise, I show the number in that cell
                else:
                    print(f"{self.board[i][j]}", end=" ")
            # After each row, I add a line to make the board look nice
            print("\n" + "-" * 5)

    def squareIsEmpty(self, row, col):
        # I'm checking if a square is available by seeing if it contains 0
        return self.board[row][col] == 0

    def update(self, row, col, num):
        # I'm trying to place a number on the board
        if self.squareIsEmpty(row, col):
            # If the square is empty, I can place the number
            self.board[row][col] = num
            return True
        else:
            # If it's already taken, I return False
            return False

    def boardFull(self):
        # I'm checking each row to see if there are any empty spaces left
        for row in self.board:
            if 0 in row:
                return False
        # If I didn't find any zeros, the board must be full
        return True

    def isWinner(self):
        # I'm checking all possible winning combinations
        for i in range(self.size):
            # First I check each row and column
            row_sum = sum(self.board[i])
            col_sum = sum(self.board[j][i] for j in range(self.size))
            
            # A row wins if it sums to 15 and all numbers are odd
            if row_sum == 15 and all(num % 2 == 1 for num in self.board[i]):
                return True
            # Same for columns
            elif col_sum == 15 and all(num % 2 == 1 for num in (self.board[j][i] for j in range(self.size))):
                return True
        
        # Now I'm checking both diagonals
        diagonal1_sum = sum(self.board[i][i] for i in range(self.size))
        diagonal2_sum = sum(self.board[i][self.size - i - 1] for i in range(self.size))
        
        # Checking if either diagonal wins
        if diagonal1_sum == 15 and all(num % 2 == 1 for num in (self.board[i][i] for i in range(self.size))):
            return True
        elif diagonal2_sum == 15 and all(num % 2 == 1 for num in (self.board[i][self.size - i - 1] for i in range(self.size))):
            return True
        
        # If no winning combination was found, return False
        return False