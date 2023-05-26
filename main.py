from TicTacToe import TicTacToe
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root,board_size=6)
    root.mainloop()
