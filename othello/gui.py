import tkinter as tk
from tkinter import messagebox


import game 

class OthelloUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Othello")
        
        self.board = game.OthelloBoard()
        
        # Create a grid of buttons for the board
        self.buttons = []
        for i in range(8):
            row = []
            for j in range(8):
                button = tk.Button(self.master, text="-", width=5, height=2, command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
        
        self.update_board()

    def update_board(self):
        for i in range(8):
            for j in range(8):
                move = i * 8 + j
                if (self.board.black >> move) & 1:
                    self.buttons[i][j].config(text="B", bg="black", fg="white")
                elif (self.board.white >> move) & 1:
                    self.buttons[i][j].config(text="W", bg="white", fg="black")
                else:
                    self.buttons[i][j].config(text="-", bg="green", fg="black")

    def make_move(self, i, j):
        move = i * 8 + j
        if self.board.make_move(move):
            self.update_board()
        else:
            messagebox.showerror("Invalid Move", "This move is not valid. Try again.")

if __name__ == "__main__":
    root = tk.Tk()
    ui = OthelloUI(root)
    root.mainloop()