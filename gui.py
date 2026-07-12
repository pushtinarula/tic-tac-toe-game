import tkinter as tk
from tkinter import messagebox
import random 

class TicTacToe:
    
    # Constructor - runs automatically when the object is created
    def __init__(self, root):
        # Create a 3x3 game board filled with empty spaces
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        # Store the main application window
        self.root = root
        self.root.title("Tic-Tac-Toe") 

        # X always starts first
        self.currentPlayer = 'X'

        # Store references to all GUI buttons
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        # Create the game board on the screen
        self.createBoard()
    
    # Create the Tic-Tac-Toe grid and Restart button
    def createBoard(self):
        # Create 3x3 buttons
        for row in range(3):
            for col in range(3):

                # lambda stores the current row and column for each button
                button = tk.Button(
                    self.root,
                    text="",
                    font=("Arial",24),
                    width=5,
                    height=2,
                    command=lambda r=row,c=col:self.makeMoves(r,c)
                )

                # Place button in the window
                button.grid(row = row, column = col)

                # Save button reference for future updates
                self.buttons[row][col] = button

        # Restart button
        restartButton = tk.Button(
            self.root,
            text="RESTART",
            font=("Arial",14),
            command=self.restartGame
        )
        restartButton.grid(row = 3, column = 0, columnspan = 3, sticky = "nsew")
    
    # Executes whenever the player clicks a square
    def makeMoves(self,row,col):
        # Only allow move if square is empty
        if self.board[row][col] != ' ':
            return        
        self.board[row][col] = 'X'
        self.buttons[row][col]["text"] = 'X'

        # Check if player wins
        if self.checkWinner():
            messagebox.showinfo("Game Over", "You Win!")
            self.restartGame()
            return
        
        # Check if game is a draw
        if self.checkDraw():
            messagebox.showinfo("Game Over", "Draw!")
            self.restartGame()
            return
        
        # Give computer its turn
        self.computerMove()
    
    # Computer AI
    def computerMove(self):
        # Try to win
        for r in range(3):
            for c in range(3):

                if self.board[r][c] == ' ':

                    # Pretend to place O
                    self.board[r][c] = 'O'

                    # If this move wins, keep it
                    if self.checkWinner():
                        self.buttons[r][c]["text"] = 'O'
                        messagebox.showinfo("Game Over", "Computer Wins!")
                        self.restartGame()
                        return
                    
                    # Otherwise undo the move
                    self.board[r][c] = ' '

        # Block player
        for r in range(3):
            for c in range(3):

                if self.board[r][c] == ' ':

                    # Pretend player places X
                    self.board[r][c] = 'X'

                    # If player would win here,
                    # place O to block that position
                    if self.checkWinner():
                        self.board[r][c] = 'O'
                        self.buttons[r][c]["text"] = 'O'
                        
                        # Check if board is full after blocking
                        if self.checkDraw():
                            messagebox.showinfo("Game Over", "Draw!")
                            self.restartGame()
                        return
                    
                    # Undo simulated move
                    self.board[r][c] = ' '

        # Random move
        # Create a list of all empty cells
        empty = [
                (r, c) 
                for r in range(3) 
                for c in range(3)
                if self.board[r][c] == ' '
        ]

        # Choose one randomly
        if empty:
            r, c = random.choice(empty)
            self.board[r][c] = 'O'
            self.buttons[r][c]["text"] = 'O'

        # Check if the game ended in a draw after the computer's move
        if self.checkDraw():
            messagebox.showinfo("Game Over", "Draw!")
            self.restartGame()
    
    # Check whether anyone has won
    def checkWinner(self):
        for i in range(3):
            # checking each row
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            # checking each column
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        # checking main diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        # checking opposite diagonal
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        
        # No winner found
        return False
    
    # Check if every square has been filled
    def checkDraw(self):
        # If any empty space remains, the game is not a draw
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True
    
    # Reset the game board
    def restartGame(self):
        # Player starts again
        self.currentPlayer = 'X'

        # Reset internal board
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        # Clear all button text
        for row in self.buttons:
            for button in row:
                button["text"] = ""