'''
Tic-Tac-Toe Game
'''
import random

class TicTacToe:

    def play(self):
        print("Game Started!!")

     # Constructor - runs automatically when the object is created
    def __init__(self):
        # Create a 3x3 game board filled with empty spaces
        self.board=[[' ' for _ in range(3)] for _ in range(3)]

        # X always starts first
        self.currentPlayer='X'

    def displayBoard(self):
        for cell in self.board:
            print('|'.join(cell))
            print('-'*5)

    def makeMoves(self, row, col):
        if(self.board[row][col] == ' '):
            self.board[row][col]=self.currentPlayer
            return True
        else:
            print("Cell already occupied.")
            return False

    def getEmptycell(self):
        emptycell=[]
        for row in range(3):
            for col in range(3):
                if(self.board[row][col] == ' '):
                    emptycell.append((row,col))
        return emptycell

    def computerMoves(self):
        empty_cells = self.getEmptycell()
        if(empty_cells):
            row,col=random.choice(empty_cells)
            self.board[row][col]='O'

    def checkWinner(self):
        for i in range(0,3):
            if(self.board[i][0] == self.board[i][1] == self.board[i][2] != ' '):
                return True
            if(self.board[0][i] == self.board[1][i] == self.board[2][i] !=' '):
                return True
        if(self.board[0][0] == self.board[1][1] == self.board[2][2] != ' '):
            return True
        if(self.board[0][2] == self.board[1][1] == self.board[2][0] != ' '):
            return True
        return False

    def checkDraw(self):
        for cell in self.board:
            if ' ' in cell:
                return False
        return True

    def playGame(self):
        while True:
            self.displayBoard()
            print("Player", self.currentPlayer, "turn")
            try:
                row=int(input("Enter row (0-2): "))
                col=int(input("Enter col (0-2): "))
            except ValueError:
                print("Invalid input! Enter numbers only.")
                continue
            if row not in range(3) or col not in range(3):
                print("Out of bounds! Try again.")
                continue
            if not self.makeMoves(row,col):
                continue
            if self.checkWinner():
                self.displayBoard()
                print(f"Player {self.currentPlayer} Wins")
                break
            if self.checkDraw() == True:
                self.displayBoard()
                print("Draw")
                break
            print("Computer's turn")
            self.computerMoves()
            if self.checkWinner():
                self.displayBoard()
                print("Computer (O) Wins")
                break
            if self.checkDraw() == True:
                self.displayBoard()
                print("Draw")
                break