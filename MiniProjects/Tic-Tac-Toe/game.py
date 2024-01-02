def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check columns
            return True
    if all([board[i][i] == player for i in range(3)]):  # Check diagonal
        return True
    if all([board[i][2-i] == player for i in range(3)]):  # Check anti-diagonal
        return True
    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        row = int(input(f"Player {players[current_player]}, enter row (0-2): "))
        col = int(input(f"Player {players[current_player]}, enter column (0-2): "))

        if board[row][col] != " ":
            print("That position is already taken! Try again.")
            continue

        board[row][col] = players[current_player]

        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = (current_player + 1) % 2


play_tic_tac_toe()
