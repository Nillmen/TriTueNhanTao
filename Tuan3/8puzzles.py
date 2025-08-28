import tkinter as tk
import numpy as np

puzzle_sizes = np.array([8, 15, 24])
size_selected = puzzle_sizes[0]   # 8-puzzle (3x3)

confusion_step = 500

# Tạo ma trận số
numbers = np.arange(1, size_selected + 2).reshape(
    int(np.sqrt(size_selected + 1)), int(np.sqrt(size_selected + 1))
)
numbers[-1, -1] = 0   # ô trống

status_win_numbers = np.copy(numbers)

buttons = []  # list 2D chứa button

def confuse(confusion_step):
    global numbers
    rows, cols = numbers.shape
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    old_l, old_n = None, None

    for _ in range(confusion_step):
        l, n = np.where(numbers == 0)
        l, n = l[0], n[0]

        i = np.random.randint(0, 4)
        new_l = l + dx[i]
        new_n = n + dy[i]

        while not (0 <= new_l < rows and 0 <= new_n < cols) or (new_l == old_l and new_n == old_n):
            i = np.random.randint(0, 4)
            new_l = l + dx[i]
            new_n = n + dy[i]
        numbers[new_l, new_n], numbers[l, n] = numbers[l, n], numbers[new_l, new_n]
        old_l, old_n = l, n
    
def check_win():
    global numbers, status_win_numbers
    return np.array_equal(numbers, status_win_numbers)

def reset_game():
    global numbers, count
    confuse(confusion_step)
    for l in range(numbers.shape[0]):
        for n in range(numbers.shape[1]):
            text = str(numbers[l, n]) if numbers[l, n] != 0 else ''
            buttons[l][n].config(text=text, bg='SystemButtonFace')

def move(l, n):
    global numbers, buttons
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(4):
        new_l = l + dx[i]
        new_n = n + dy[i]

        if 0 <= new_l < numbers.shape[0] and 0 <= new_n < numbers.shape[1] and numbers[new_l, new_n] == 0:  # tìm được ô trống
            numbers[new_l, new_n], numbers[l, n] = numbers[l, n], numbers[new_l, new_n]

            # cập nhật giao diện
            buttons[new_l][new_n].config(text=str(numbers[new_l, new_n]))
            buttons[l][n].config(text='')

            break
        elif i == 3:  # không tìm được ô trống
            buttons[l][n].config(bg='red')
            buttons[l][n].after(300, lambda: buttons[l][n].config(bg='SystemButtonFace'))

    if check_win():
        for row in buttons:
            for button in row:
                button.config(bg='lightgreen')
                button.after(300, lambda : reset_game())
                
        

def on_click_button(l, n):
    move(l, n)

def create_buttons(root):
    global buttons
    buttons = []   # reset danh sách
    rows, cols = numbers.shape
    for l in range(rows):
        row_buttons = []
        for n in range(cols):
            text = str(numbers[l, n]) if numbers[l, n] != 0 else ''
            button = tk.Button(
                root,
                text=text,
                font=('Arial', 24),
                command=lambda l=l, n=n: on_click_button(l, n) 
            )
            button.grid(row=l, column=n, padx=5, pady=5, sticky='nsew')
            row_buttons.append(button)
        buttons.append(row_buttons)

def main():
    global confusion_step, count
    root = tk.Tk()
    root.title("8-Puzzle Game")
    root.geometry("400x400")
    root.minsize(200, 200)
    root.maxsize(800, 800)
    root.configure(bg='lightgrey')

    # cho phép grid co giãn
    for i in range(numbers.shape[0]):
        root.grid_rowconfigure(i, weight=1)
    for j in range(numbers.shape[1]):
        root.grid_columnconfigure(j, weight=1)

    confuse(confusion_step)
    create_buttons(root)

    root.mainloop()

if __name__ == "__main__":
    main()