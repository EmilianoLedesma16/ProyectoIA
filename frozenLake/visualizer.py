import customtkinter as ctk
from tkinter import messagebox
from frozenLake.enviroment import FrozenLakeEnv
from frozenLake.bfs import bfs
from frozenLake.dfs import dfs
import time

class FrozenLakeGUI(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("FrozenLake - Resolución con Búsqueda")
        self.geometry("600x750")
        self.resizable(False, False)
        self.env = FrozenLakeEnv()
        self.path = []
        self.explored = []
        self.create_widgets()
        self.draw_grid()

    def create_widgets(self):
        ctk.CTkLabel(self, text="FrozenLake - Resolución con Búsqueda", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        frame = ctk.CTkFrame(self)
        frame.pack(pady=5)
        self.alg_var = ctk.StringVar(value="BFS")
        self.size_var = ctk.StringVar(value="4x4")
        ctk.CTkLabel(frame, text="Algoritmo:", font=ctk.CTkFont(size=15)).grid(row=0, column=0, padx=10, pady=5)
        ctk.CTkRadioButton(frame, text="BFS", variable=self.alg_var, value="BFS").grid(row=0, column=1, padx=5)
        ctk.CTkRadioButton(frame, text="DFS", variable=self.alg_var, value="DFS").grid(row=0, column=2, padx=5)
        ctk.CTkLabel(frame, text="Tamaño:", font=ctk.CTkFont(size=15)).grid(row=1, column=0, padx=10, pady=5)
        ctk.CTkRadioButton(frame, text="4x4", variable=self.size_var, value="4x4", command=self.set_board_size).grid(row=1, column=1, padx=5)
        ctk.CTkRadioButton(frame, text="8x8", variable=self.size_var, value="8x8", command=self.set_board_size).grid(row=1, column=2, padx=5)
        ctk.CTkButton(self, text="Ejecutar", command=self.solve_and_animate).pack(pady=8)
        ctk.CTkButton(self, text="Mostrar solo solución óptima", command=self.show_optimal).pack(pady=2)
        self.result_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=14))
        self.result_label.pack(pady=5)
        self.canvas = ctk.CTkCanvas(self, width=480, height=480, bg="white")
        self.canvas.pack(pady=15)

    def set_board_size(self):
        size = self.size_var.get()
        if size == "4x4":
            self.env.set_grid(self.env.default_4x4)
        else:
            self.env.set_grid(self.env.default_8x8)
        self.path = []
        self.explored = []
        self.result_label.configure(text="")
        self.draw_grid()

    def draw_grid(self, path=None, explored=None):
        self.canvas.delete("all")
        n, m = self.env.n, self.env.m
        cell_size = 480 // max(n, m)
        for i in range(n):
            for j in range(m):
                x0, y0 = j*cell_size, i*cell_size
                x1, y1 = x0+cell_size, y0+cell_size
                val = self.env.grid[i][j]
                # Colores: libre, hueco, inicio, meta
                color = "#bde0fe" if val == 0 else "#ffafcc" if val == 1 else "#b7e4c7" if val == 2 else "#ffd60a"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")
        # Celdas exploradas
        if explored:
            for (i, j) in explored:
                x0, y0 = j*cell_size, i*cell_size
                x1, y1 = x0+cell_size, y0+cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, fill="#e0e0e0", outline="black")
        # Dibuja el camino si existe
        if path:
            for (i, j) in path:
                x0, y0 = j*cell_size, i*cell_size
                x1, y1 = x0+cell_size, y0+cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, fill="#90e0ef", outline="black")
        # Redibuja inicio y meta
        si, sj = self.env.start
        gi, gj = self.env.goal
        self.canvas.create_rectangle(sj*cell_size, si*cell_size, (sj+1)*cell_size, (si+1)*cell_size, fill="#b7e4c7", outline="black")
        self.canvas.create_rectangle(gj*cell_size, gi*cell_size, (gj+1)*cell_size, (gi+1)*cell_size, fill="#ffd60a", outline="black")

    def solve_and_animate(self):
        alg = self.alg_var.get()
        if alg == "BFS":
            path, explored = bfs(self.env, return_explored=True)
        else:
            path, explored = dfs(self.env, return_explored=True)
        self.path = path
        self.explored = explored
        if not path:
            self.result_label.configure(text="No se encontró un camino hasta la meta.")
            self.draw_grid()
            return
        self.result_label.configure(text=f"Pasos dados: {len(path)-1} | Camino óptimo {'(BFS)' if alg=='BFS' else ''}")
        # Animación de exploración
        for idx in range(1, len(explored)+1):
            self.draw_grid(path=None, explored=explored[:idx])
            self.update()
            time.sleep(0.03)
        # Animación del camino
        for idx in range(1, len(path)+1):
            self.draw_grid(path=path[:idx], explored=explored)
            self.update()
            time.sleep(0.15)

    def show_optimal(self):
        # Solo muestra el camino óptimo (BFS)
        path, explored = bfs(self.env, return_explored=True)
        self.path = path
        self.explored = explored
        if not path:
            self.result_label.configure(text="No se encontró un camino hasta la meta.")
            self.draw_grid()
            return
        self.result_label.configure(text=f"Pasos dados: {len(path)-1} | Camino óptimo (BFS)")
        self.draw_grid(path=path, explored=None)

def launch_frozenlake_gui():
    FrozenLakeGUI()