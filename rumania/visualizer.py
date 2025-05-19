import customtkinter as ctk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from rumania.graph import get_romania_graph, get_heuristics
from rumania.greedy import greedy_search
from rumania.astar import astar_search
from rumania.hill_climbing import hill_climbing

class RumaniaGUI(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Mapa de Rumania - Algoritmos Informados")
        self.geometry("900x700")
        self.resizable(False, False)
        self.G, self.positions = get_romania_graph()
        self.heuristics = get_heuristics()
        self.path = []
        self.create_widgets()
        self.draw_graph()

    def create_widgets(self):
        frame = ctk.CTkFrame(self)
        frame.pack(pady=10)
        self.alg_var = ctk.StringVar(value="Greedy")
        self.start_var = ctk.StringVar(value="Arad")
        self.goal_var = ctk.StringVar(value="Bucharest")
        ctk.CTkLabel(frame, text="Algoritmo:", font=ctk.CTkFont(size=15)).grid(row=0, column=0, padx=10)
        ctk.CTkRadioButton(frame, text="Greedy", variable=self.alg_var, value="Greedy").grid(row=0, column=1)
        ctk.CTkRadioButton(frame, text="A*", variable=self.alg_var, value="A*").grid(row=0, column=2)
        ctk.CTkRadioButton(frame, text="Hill Clambing", variable=self.alg_var, value="Hill Clambing").grid(row=0, column=3)
        ctk.CTkLabel(frame, text="Inicio:", font=ctk.CTkFont(size=15)).grid(row=1, column=0, padx=10)
        ctk.CTkOptionMenu(frame, variable=self.start_var, values=list(self.G.nodes)).grid(row=1, column=1)
        ctk.CTkLabel(frame, text="Meta:", font=ctk.CTkFont(size=15)).grid(row=1, column=2, padx=10)
        ctk.CTkOptionMenu(frame, variable=self.goal_var, values=list(self.G.nodes)).grid(row=1, column=3)
        ctk.CTkButton(self, text="Ejecutar", command=self.solve_and_draw).pack(pady=10)
        self.result_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=14))
        self.result_label.pack(pady=5)
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack()

    def draw_graph(self, path=None):
        self.ax.clear()
        nx.draw(self.G, pos=self.positions, ax=self.ax, with_labels=True, node_color="#bde0fe", node_size=600, font_weight='bold')
        nx.draw_networkx_edge_labels(self.G, pos=self.positions, ax=self.ax, edge_labels=nx.get_edge_attributes(self.G, 'weight'))
        if path:
            # Resalta el camino encontrado
            path_edges = list(zip(path, path[1:]))
            nx.draw_networkx_nodes(self.G, pos=self.positions, nodelist=path, ax=self.ax, node_color="#ffd60a", node_size=700)
            nx.draw_networkx_edges(self.G, pos=self.positions, edgelist=path_edges, ax=self.ax, edge_color="#ff6f61", width=3)
        self.canvas.draw()

    def solve_and_draw(self):
        start = self.start_var.get()
        goal = self.goal_var.get()
        alg = self.alg_var.get()
        if alg == "Greedy":
            path = greedy_search(self.G, self.heuristics, start, goal)
        elif alg == "A*":
            path = astar_search(self.G, self.heuristics, start, goal)
        else:
            path = hill_climbing(self.G, self.heuristics, start, goal)
        if not path:
            self.result_label.configure(text="No se encontró un camino.")
        else:
            self.result_label.configure(text=f"Camino encontrado: {' → '.join(path)}")
        self.draw_graph(path=path)

def launch_rumania_gui():
    RumaniaGUI()