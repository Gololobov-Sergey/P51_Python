import random
import os

board = [[' ' for i in range(3)] for j in range(3)]

def print_board(board):
    for i in range(9):
        print(board[i // 3][i % 3], end=' ')
        if (i + 1) % 3 == 0:
            print()
            if i != 9 - 1:
                print("__|___|__")
        else:
            print("|", end=' ')


def isWinner(board):
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != ' ':
        return board[0][0]
    if board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != ' ':
        return board[1][0]
    if board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != ' ':
        return board[2][0]
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != ' ':
        return board[0][0]
    if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != ' ':
        return board[0][1]
    if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != ' ':
        return board[0][2]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return ' '


move = 0
while move != 9:
    os.system("cls")
    print_board(board)
    print()
    choice = int(input("1-9 : ")) - 1
    sym = 'X' if move % 2 == 0 else '0'
    board[choice//3][choice%3] = sym
    move += 1
    if isWinner(board) != ' ':
        break

os.system("cls")
print_board(board)
if isWinner(board) == ' ':
    print("Draw")
else:
    print("Winner", isWinner(board))




# print(arr)

# for i in range(3):
#     for j in range(3):
#         print(arr[i][j], end=' ')
#     print()



# for i in range(9):
#     print(arr[i//3][i%3], end=' ')
#     if (i+1) % 3 == 0:
#         print()

