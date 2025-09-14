import tkinter as tk
import random
import heapq

def is_safe(state, row, col):
    for r, c in enumerate(state):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def solve_n_queens_all(n=8):
    sols = []
    def backtrack(state):
        row = len(state)
        if row == n:
            sols.append(tuple(state))
            return
        for col in range(n):
            if is_safe(state, row, col):
                state.append(col)
                backtrack(state)
                state.pop()
    backtrack([])
    return sols

class BoardCanvas:
    def __init__(self, parent, n=8, cell_size=40):
        self.n = n
        self.cell = cell_size
        self.canvas = tk.Canvas(parent, width=n*cell_size, height=n*cell_size)
        self.canvas.pack()
        self.queen_items = []
        self._draw_grid()

    def _draw_grid(self):
        self.canvas.delete("cell")
        for r in range(self.n):
            for c in range(self.n):
                x1, y1 = c*self.cell, r*self.cell
                x2, y2 = x1+self.cell, y1+self.cell
                color = "white" if (r+c)%2==0 else "gray"
                self.canvas.create_rectangle(x1,y1,x2,y2, fill=color, tags="cell")

    def clear_queens(self):
        for item in self.queen_items:
            self.canvas.delete(item)
        self.queen_items = []

    def show_partial(self, state, color="red"):
        self.clear_queens()
        for r, c in enumerate(state):
            cx = c*self.cell + self.cell/2
            cy = r*self.cell + self.cell/2
            tid = self.canvas.create_text(cx, cy, text="Q", font=("Arial", 16, "bold"), fill=color)
            self.queen_items.append(tid)

    def flash_green(self):
        self.canvas.config(bg="lightgreen")
        self.canvas.after(400, lambda: self.canvas.config(bg="white"))

def calc_attack_cost(row, col, path):
    total_cost = 0
    # tập hợp các vị trí quân hậu đã đặt để bỏ qua
    occupied = {(r, c) for r, c, _ in path}

    # lấy quân hậu cuối trong path để tính khoảng cách
    if not path:
        r_last, c_last = 0, 0  # nếu chưa có quân hậu nào
    else:
        r_last, c_last, _ = path[-1]

    total_cost = abs(row - r_last) + abs(col - c_last)

    return total_cost

def ucs_steps(goal, n=8):
    # Priority queue
    pq = []
    # chi phí 0, trạng thái rỗng(chưa đặt hậu) và path(row, col, chi phi)
    heapq.heappush(pq, (0, [], []))  #(cost, state, path)

    while pq:
        cost, state, path = heapq.heappop(pq)
        row = len(state)

        if row == n:
            if tuple(state) == goal:
                yield state, True, path 
                return
            continue

        for col in range(n):
            if is_safe(state, row, col):
                new_state = state + [col]
                step_cost = calc_attack_cost(row, col, path)
                new_cost = cost + step_cost
                new_path = path + [(row, col, step_cost)] 

                yield new_state, False, new_path
                heapq.heappush(pq, (new_cost, new_state, new_path))

def main():
    root = tk.Tk()
    root.title("N-Queens")
    
    frame = tk.Frame(root)
    frame.pack()
    board_left = BoardCanvas(frame, n=8, cell_size=40)
    board_right = BoardCanvas(frame, n=8, cell_size=40)

    all_sols = solve_n_queens_all(8)
    goal_holder = {"sol": None, "gen": None}

    def random_goal():
        sol = random.choice(all_sols)
        goal_holder["sol"] = sol
        board_right.show_partial(sol, color="blue")
        board_left.clear_queens()

    def run():
        sol = goal_holder.get("sol")
        if not sol: return
        goal_holder["gen"] = ucs_steps(sol, 8)
        step()

    def step():
        gen = goal_holder.get("gen")
        if not gen: return
        try:
            state, done, path = next(gen)
            board_left.show_partial(state, color="red")
            if done:
                board_left.flash_green()
                sum_chi_phi = 0
                for i in range(len(path)):
                    print(f"Đặt quân hậu thứ {i + 1} vào hàng {path[i][0] + 1}, cột {path[i][1] + 1} có chi phí {path[i][2]}")
                    sum_chi_phi += path[i][2]
                print("Tổng chi phí:", sum_chi_phi)
                return
            root.after(10, step)
        except StopIteration:
            return

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Random Goal", command=random_goal).pack(side="left", padx=10, pady=10)
    tk.Button(btn_frame, text="Run", command=run).pack(side="left", padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
