from ticTacToe.game_logic import check_winner, is_full, get_valid_moves
import copy

def minimax_ab(board, is_maximizing, alpha=-float("inf"), beta=float("inf")):
    winner = check_winner(board)
    if winner == "O":
        return 1, None
    elif winner == "X":
        return -1, None
    elif is_full(board):
        return 0, None

    best_move = None
    if is_maximizing:
        best_score = -float("inf")
        for i, j in get_valid_moves(board):
            new_board = copy.deepcopy(board)
            new_board[i][j] = "O"
            score, _ = minimax_ab(new_board, False, alpha, beta)
            if score > best_score:
                best_score = score
                best_move = (i, j)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score, best_move
    else:
        best_score = float("inf")
        for i, j in get_valid_moves(board):
            new_board = copy.deepcopy(board)
            new_board[i][j] = "X"
            score, _ = minimax_ab(new_board, True, alpha, beta)
            if score < best_score:
                best_score = score
                best_move = (i, j)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score, best_move