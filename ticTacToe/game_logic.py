def check_winner(board):
    # Filas, columnas y diagonales
    lines = [board[i] for i in range(3)] + \
            [[board[i][j] for i in range(3)] for j in range(3)] + \
            [[board[i][i] for i in range(3)], [board[i][2-i] for i in range(3)]]
    for line in lines:
        if line[0] != "" and all(cell == line[0] for cell in line):
            return line[0]
    return None

def is_full(board):
    return all(cell != "" for row in board for cell in row)

def get_valid_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]