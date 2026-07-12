from generator import TicTacToe
from gui import TicTacToe
import tkinter as tk

if __name__=="__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

    game = TicTacToe(root)
    game.play()