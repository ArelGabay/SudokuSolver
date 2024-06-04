import functions
import tkinter as tk
from tkinter import ttk


def solve_sudoku_gui(entries):
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    for r in range(9):
        row_values = []
        for c in range(9):
            value = entries[r][c].get()
            row_values.append(int(value))
        board[r] = row_values

    functions.solve(board)
    update_gui(board)


def update_gui(board):
    clear_window()
    for r in range(9):
        for c in range(9):
            value = board[r][c]
            label = tk.Label(window, text=value, relief=tk.RIDGE, width=8, height=3)
            label.grid(row=r, column=c, padx=2, pady=2)


def clear_window():
    for widget in window.winfo_children():
        widget.destroy()


def create_window():
    window.title("Sudoku")

    # Create a 9x9 grid using ttk
    frame = ttk.Frame(window, padding=10)
    frame.grid()

    # Create a 9x9 grid of entry widgets
    entries = []
    for i in range(9):
        row = []
        for j in range(9):
            entry = tk.Entry(window, width=2, font=('Arial', 16, 'bold'), justify='center')
            entry.grid(row=i, column=j, padx=2, pady=2)
            row.append(entry)
        entries.append(row)

    solve_button = tk.Button(window, text="Solve", command=lambda: solve_sudoku_gui(entries))
    solve_button.grid(row=9, column=0, columnspan=9, pady=10)


# Start the Tkinter event loop
window = tk.Tk()
create_window()
window.mainloop()
