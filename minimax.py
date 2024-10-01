board = ['' for _ in range(9)]

def print_board():
    print("______")
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("______")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("______")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print("______")

def is_full(board):
    return '' not in board

def is_winner(board, player):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def minimax(board, depth, is_maximizing):
    scores = {'x': 1, 'o': -1, 'tie': 0}
    if is_winner(board, 'x'):
        return scores['x'] - depth
    if is_winner(board, 'o'):
        return scores['o'] + depth
    if is_full(board):
        return scores['tie']
    
    if is_maximizing:
        best_score = float("-inf")
        for i in range(9):
            if board[i] == '':
                board[i] = 'x'
                score = minimax(board, depth + 1, False)
                board[i] = ''
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == '':
                board[i] = 'o'
                score = minimax(board, depth + 1, True)
                board[i] = ''
                best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_move = -1
    best_score = float('-inf')
    for i in range(9):
        if board[i] == '':
            board[i] = 'x'
            score = minimax(board, 0, False)
            board[i] = ''
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

while True:
    print_board()
    move = int(input("Enter your move (0-8): "))
    if board[move] != '':
        print("Invalid move")
        continue
    board[move] = 'o'
    if is_winner(board, 'o'):
        print_board()
        print("You win!")
        break
    if is_full(board):
        print_board()
        print("It's a tie!")
        break
    best_move = find_best_move(board)
    board[best_move] = 'x'
    if is_winner(board, 'x'):
        print_board()
        print("Computer wins!")
        break
    if is_full(board):
        print_board()
        print("It's a tie!")
        break