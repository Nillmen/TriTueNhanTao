import numpy as np
import tkinter as tk
import random

class square_button:
    def __init__(self, x, y, color, available=True):
        self.x = x
        self.y = y
        self.color = color
        self.available = available
        self.is_queen = False  

def create_board():
    board = np.empty((8, 8), dtype=object)
    for i in range(8):
        for j in range(8):
            color = 'white' if (i + j) % 2 == 0 else 'black'
            board[i, j] = square_button(i, j, color)
    return board

def creat_buttons(parent, board):
    buttons = []
    for i in range(8):
        row_buttons = []
        for j in range(8):
            button = tk.Button(
                parent,
                bg=board[i, j].color,
                command=lambda x=i, y=j: on_click_button(board, buttons, x, y)
            )
            button.grid(row=i, column=j, padx=2, pady=2, sticky='nsew')
            row_buttons.append(button)
        buttons.append(row_buttons)

    for i in range(8):
        parent.grid_rowconfigure(i, weight=1)
        parent.grid_columnconfigure(i, weight=1)
    return buttons

def update_availability(board):
    """Tính lại các ô available dựa trên vị trí hậu hiện có"""
    # Reset tất cả về True
    for i in range(8):
        for j in range(8):
            board[i, j].available = True

    dx_y = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0), (1, 1)]

    for x in range(8):
        for y in range(8):
            if board[x, y].is_queen:
                board[x, y].available = False
                for dx, dy in dx_y:
                    for k in range(1, 8):
                        nx, ny = x + dx*k, y + dy*k
                        if 0 <= nx < 8 and 0 <= ny < 8:
                            board[nx, ny].available = False
                        else:
                            break

def put_queen(board, buttons, x, y):
    board[x, y].is_queen = True
    buttons[x][y].config(text='Q', fg='red')
    update_availability(board)

def remove_queen(board, buttons, x, y):
    board[x, y].is_queen = False
    buttons[x][y].config(text='')
    update_availability(board)

def on_click_button(board, buttons, x, y):
    if not board[x, y].is_queen and board[x, y].available:
        put_queen(board, buttons, x, y)
    elif board[x, y].is_queen:
        remove_queen(board, buttons, x, y)

def clear_board(board, buttons):
    for i in range(8):
        for j in range(8):
            board[i, j].is_queen = False
            buttons[i][j].config(text='')
    update_availability(board)

def k_queens_positions(k, n=8):
    """Tìm ngẫu nhiên k hậu không ăn nhau trên bàn n×n (k <= n)."""
    cols = list(range(n))
    random.shuffle(cols) 

    used_rows = set()
    used_d1 = set() 
    used_d2 = set()  
    pos = []

    def backtrack(ci, placed):
        if placed == k:
            return True
        if ci == n:
            return False

        col = cols[ci]
        rows = list(range(n))
        random.shuffle(rows)  # ngẫu nhiên thứ tự hàng

        # Thử đặt ở cột này
        for row in rows:
            if row in used_rows or (row - col) in used_d1 or (row + col) in used_d2:
                continue
            used_rows.add(row); used_d1.add(row - col); used_d2.add(row + col)
            pos.append((row, col))
            if backtrack(ci + 1, placed + 1):
                return True
            pos.pop()
            used_rows.remove(row); used_d1.remove(row - col); used_d2.remove(row + col)

        return backtrack(ci + 1, placed)

    ok = backtrack(0, 0)
    return pos if ok else None

def random_queen(buttons, board, quantity):
    """Đặt quantity hậu ngẫu nhiên, đảm bảo không ăn nhau (nếu có lời giải)."""
    sol = k_queens_positions(quantity, 8)
    if not sol:
        print(f"⚠️ Không tìm được cấu hình cho {quantity} hậu.")
        return
    clear_board(board, buttons)
    for x, y in sol:
        put_queen(board, buttons, x, y) 
def main():
    root = tk.Tk()
    root.title("Two Chess Boards")
    root.geometry("1800x1600")
    root.configure(bg="lightgrey")

    frame1 = tk.Frame(root, bg="grey")
    frame1.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    frame2 = tk.Frame(root, bg="grey")
    frame2.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)

    board1 = create_board()
    buttons1 = creat_buttons(frame1, board1)

    board2 = create_board()
    buttons2 = creat_buttons(frame2, board2)

    random_queen(buttons2, board2, 8)

    root.mainloop()

if __name__ == "__main__":
    main()