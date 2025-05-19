import customtkinter as ctk

from frozenLake.visualizer import launch_frozenlake_gui
from rumania.visualizer import launch_rumania_gui
from ticTacToe.gui import launch_tictactoe_gui

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class MainMenu(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("IA - Resolución de Problemas Clásicos")
        self.geometry("420x380")
        self.resizable(False, False)
        self.configure(bg="#f0f0f0")
        self.create_widgets()

    def create_widgets(self):
        title = ctk.CTkLabel(self, text="Selecciona un problema", font=ctk.CTkFont(size=22, weight="bold"))
        title.pack(pady=35)

        btn_frozenlake = ctk.CTkButton(self, text="1. FrozenLake (Laberinto)", command=self.open_frozenlake, width=220, height=40)
        btn_frozenlake.pack(pady=12)

        btn_rumania = ctk.CTkButton(self, text="2. Mapa de Rumania (Grafos)", command=self.open_rumania, width=220, height=40)
        btn_rumania.pack(pady=12)

        btn_tictactoe = ctk.CTkButton(self, text="3. Gato (Tic-Tac-Toe)", command=self.open_tictactoe, width=220, height=40)
        btn_tictactoe.pack(pady=12)

        credits = ctk.CTkLabel(self, text="Proyecto IA ESCOM 2025", font=ctk.CTkFont(size=12, slant="italic"), text_color="#888")
        credits.pack(side="bottom", pady=18)

    def open_frozenlake(self):
        launch_frozenlake_gui()

    def open_rumania(self):
        launch_rumania_gui()

    def open_tictactoe(self):
        launch_tictactoe_gui()

if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()