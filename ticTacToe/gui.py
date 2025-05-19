import customtkinter as ctk
from ticTacToe.game_logic import check_winner, is_full, get_valid_moves
from ticTacToe.minimax import minimax
from ticTacToe.minimax_ab import minimax_ab
import copy

class TicTacToeGUI(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe IA")
        self.geometry("400x500")
        self.resizable(False, False)
        self.board = [[""]*3 for _ in range(3)]
        self.buttons = [[None]*3 for _ in range(3)]
        self.current_player = "X"
        self.ia_starts = ctk.BooleanVar(value=False)
        self.use_ab = ctk.BooleanVar(value=False)
        self.status = ctk.StringVar(value="Turno del jugador")
        self.create_widgets()
        self.reset_board()

    def create_widgets(self):
        frame = ctk.CTkFrame(self)
        frame.pack(pady=20)
        for i in range(3):
            for j in range(3):
                btn = ctk.CTkButton(frame, text="", width=90, height=90, font=("Arial", 32),
                                    command=lambda i=i, j=j: self.player_move(i, j))
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = btn

        self.status_label = ctk.CTkLabel(self, textvariable=self.status, font=ctk.CTkFont(size=18))
        self.status_label.pack(pady=10)

        options = ctk.CTkFrame(self)
        options.pack(pady=10)
        ctk.CTkCheckBox(options, text="IA comienza", variable=self.ia_starts, command=self.reset_board).pack(side="left", padx=8)
        ctk.CTkCheckBox(options, text="Usar poda alfa-beta", variable=self.use_ab).pack(side="left", padx=8)
        ctk.CTkButton(options, text="Reiniciar", command=self.reset_board, width=100).pack(side="left", padx=8)

    def reset_board(self):
        self.board = [[""]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].configure(text="", state="normal")
        self.current_player = "O" if self.ia_starts.get() else "X"
        self.status.set("Turno de la IA" if self.current_player == "O" else "Turno del jugador")
        self.update_idletasks()
        if self.current_player == "O":
            self.after(500, self.ia_move)

    def player_move(self, i, j):
        if self.board[i][j] == "" and self.current_player == "X":
            self.board[i][j] = "X"
            self.buttons[i][j].configure(text="X")
            if self.check_end():
                return
            self.current_player = "O"
            self.status.set("Turno de la IA")
            self.after(500, self.ia_move)

    def ia_move(self):
        if self.use_ab.get():
            _, move = minimax_ab(copy.deepcopy(self.board), True)
        else:
            _, move = minimax(copy.deepcopy(self.board), True)
        if move:
            i, j = move
            self.board[i][j] = "O"
            self.buttons[i][j].configure(text="O")
        if self.check_end():
            return
        self.current_player = "X"
        self.status.set("Turno del jugador")

    def check_end(self):
        winner = check_winner(self.board)
        if winner:
            self.status.set(f"¡Ganó {'la IA' if winner == 'O' else 'el jugador'}!")
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j].configure(state="disabled")
            return True
        elif is_full(self.board):
            self.status.set("¡Empate!")
            return True
        return False

def launch_tictactoe_gui():
    TicTacToeGUI()