import random
import math

# Define the first mover
# 1 is you and -1 is the computer
first = 0
board_list = ["-" for i in range(16)]

# Reset board
def reset_board():
    global board_list  # Define the board as a global variable
    board_list = ["-" for ii in range(16)]

# Display board
def print_board():
    print("Board: ")
    for i in range(1, 17):
        if i % 4 == 0:
            print(board_list[i - 1])
        else:
            print(board_list[i - 1], end="")
    return board_list

# Define winning criteria and return the winner label
# 'O' is you and 'X' is the computer
def winner_check(board):
    if ((board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or
            (board[1] == 'X' and board[2] == 'X' and board[3] == 'X') or
            (board[4] == 'X' and board[5] == 'X' and board[6] == 'X' ) or
            (board[5] == 'X' and board[6] == 'X' and board[7] == 'X') or
            (board[8] == 'X' and board[9] == 'X' and board[10] == 'X') or
            (board[9] == 'X' and board[10] == 'X' and board[11] == 'X') or
            (board[12] == 'X' and board[13] == 'X' and board[14] == 'X') or
            (board[13] == 'X' and board[14] == 'X' and board[15] == 'X') or
            (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or
            (board[4] == 'X' and board[8] == 'X' and board[12] == 'X') or
            (board[1] == 'X' and board[5] == 'X' and board[9] == 'X') or
            (board[5] == 'X' and board[9] == 'X' and board[13] == 'X') or
            (board[2] == 'X' and board[6] == 'X' and board[10] == 'X') or
            (board[6] == 'X' and board[10] == 'X' and board[14] == 'X') or
            (board[3] == 'X' and board[7] == 'X' and board[11] == 'X') or
            (board[7] == 'X' and board[11] == 'X' and board[15] == 'X') or
            (board[0] == 'X' and board[5] == 'X' and board[10] == 'X') or
            (board[5] == 'X' and board[10] == 'X' and board[15] == 'X') or
            (board[3] == 'X' and board[6] == 'X' and board[9] == 'X') or
            (board[6] == 'X' and board[9] == 'X' and board[12] == 'X') or
            (board[1] == 'X' and board[6] == 'X' and board[11] == 'X') or
            (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or
            (board[4] == 'X' and board[9] == 'X' and board[14] == 'X') or
            (board[7] == 'X' and board[10] == 'X' and board[13] == 'X')):
        return 'X'
    elif ((board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or
            (board[1] == 'O' and board[2] == 'O' and board[3] == 'O') or
            (board[4] == 'O' and board[5] == 'O' and board[6] == 'O' ) or
            (board[5] == 'O' and board[6] == 'O' and board[7] == 'O') or
            (board[8] == 'O' and board[9] == 'O' and board[10] == 'O') or
            (board[9] == 'O' and board[10] == 'O' and board[11] == 'O') or
            (board[12] == 'O' and board[13] == 'O' and board[14] == 'O') or
            (board[13] == 'O' and board[14] == 'O' and board[15] == 'O') or
            (board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or
            (board[4] == 'O' and board[8] == 'O' and board[12] == 'O') or
            (board[1] == 'O' and board[5] == 'O' and board[9] == 'O') or
            (board[5] == 'O' and board[9] == 'O' and board[13] == 'O') or
            (board[2] == 'O' and board[6] == 'O' and board[10] == 'O') or
            (board[6] == 'O' and board[10] == 'O' and board[14] == 'O') or
            (board[3] == 'O' and board[7] == 'O' and board[11] == 'O') or
            (board[7] == 'O' and board[11] == 'O' and board[15] == 'O') or
            (board[0] == 'O' and board[5] == 'O' and board[10] == 'O') or
            (board[5] == 'O' and board[10] == 'O' and board[15] == 'O') or
            (board[3] == 'O' and board[6] == 'O' and board[9] == 'O') or
            (board[6] == 'O' and board[9] == 'O' and board[12] == 'O') or
            (board[1] == 'O' and board[6] == 'O' and board[11] == 'O') or
            (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or
            (board[4] == 'O' and board[9] == 'O' and board[14] == 'O') or
            (board[7] == 'O' and board[10] == 'O' and board[13] == 'O')):
        return 'O'
    else:
        return ''

# You input the positions
def player():
    while (1):
        print("Position to go 1-16")
        number = int(input())-1
        if board_list[number] == '-':
            board_list[number] = 'O'
            break
        else:
            print("Position filled. Choose another one. 1-16")
            continue

# The computer input the positions randomly
def computer():
    comp_moves=[]
    for index in range(len(board_list)):
        if board_list[index] == '-':
            comp_moves.append(index)
    return random.choice(comp_moves)

def make_best_move():
    bestScore = -math.inf
    bestMove = None
    for index in range(len(board_list)):
        if board_list[index] == '-':
            board_list[index] = 'X'
            count = 0
            score = minimax(board_list,0,False, count)
            print("score: ", score)
            board_list[index] = '-'
            if (score > bestScore):
                bestScore = score
                bestMove = index
    print("bestMove ", bestMove)
    return bestMove

def minimax(board_list,depth, isMaxer, count):
    print("start minimax")
    state = winner_check(board_list)
    if not board_not_full(board_list) and state == '':
        return 0
    if state=='O':
        return -10
    if state == 'X':
        return 10

    count += 1
    print("count: ", count)

    if isMaxer:
        bestScore = -math.inf
        for index1 in range(len(board_list)):
            if board_list[index1] == '-':
                print("index1 ", index1)
                board_list[index1] = 'X'
                score = minimax(board_list, depth + 1, False, count)
                board_list[index1] = '-'
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = math.inf
        for index1 in range(len(board_list)):
            if board_list[index1] == '-':
                board_list[index1] = 'O'
                score = minimax(board_list, depth + 1, True, count)
                board_list[index1] = '-'
                bestScore = min(score, bestScore)
        return bestScore

# Check if the board is full or not
# Default it is not full
def board_not_full(board):
    if board.count('-') > 1:
        return True
    else:
        return False

def main():
    print("------ Welcome to Tic-Tac-Toe Game -------\n")
    while (1):
        global first
        while (1):
            first = int(input("Choose who moves first. You:1 Computer:-1 Quit:0 \n"))
            if first == 0:
                next_move = first
                break
            if first == -1 or first == 1:
                next_move = first
                print_board()
                break
            else:
                print("Only input 1 or 0 or -1")
                continue
        if next_move == 0:
            print("You quit Tic-Tac-Toe.")
            break

        while board_not_full(board_list) and winner_check(board_list) == '':

            if next_move == 1 and board_not_full(board_list):
                player()
                next_move = -1
            if next_move == -1 and board_not_full(board_list):
                computer_move = make_best_move()
                board_list[computer_move] = 'X'
                next_move = 1
                print('Computer position is ' + str(computer_move+1))
            print_board()
            winner = winner_check(board_list)
            if winner == 'O':
                print("You won.")
                break
            if winner == 'X':
                print("Computer won.")
                break
        if not board_not_full(board_list):
            print('No one won.')
        reset_board()

main()