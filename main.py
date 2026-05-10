print("Welcome to Tic Tac Toe Game")
import random

def display(board):
    print(board[0], "|", board[1], "|", board[2])
    print("----------")
    print(board[3], "|", board[4], "|", board[5])
    print("----------")
    print(board[6], "|", board[7], "|", board[8])

#check win
def win(board, player):
    return (
        (board[0]==board[1]==board[2]==player) or
        (board[3]==board[4]==board[5]==player) or
        (board[6]==board[7]==board[8]==player) or
        (board[0]==board[3]==board[6]==player) or
        (board[1]==board[4]==board[7]==player) or
        (board[2]==board[5]==board[8]==player) or
        (board[0]==board[4]==board[8]==player) or
        (board[2]==board[4]==board[6]==player)
    )

#check draw
def draw(board):
    return " " not in board

#check free pos
def free(board, pos):
    return board[pos] == " "


def computer_move(board):
    available = [i for i in range(9) if board[i] == " "]
    return random.choice(available)


#Game start here :
while True:   #true until win or draw

    board = [" "] * 9  #new clear board

    mode = input("1- Player  2- Computer: ")
    player1 = input("Choose X or O: ").upper()

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    start = input("Do you want to start? (yes/no): ")  #who play first

    if start.upper() == "YES":
        current = player1
    else:
        current = player2

    #
    print("Positions are from 0 to 8 :")
    print("0 | 1 | 2")
    print("3 | 4 | 5")
    print("6 | 7 | 8")

    while True: #start playing
        display(board)

        #other player take action or computer
        if mode == "1" or current == player1:
            pos = int(input("Choose position (0-8): "))
        else:
            pos = computer_move(board)
            print("Computer chose:", pos)

        #if free pos play, else "not available" & ask for enter another pos
        if free(board, pos):
            board[pos] = current
        else:
            print("Not available")
            continue

        #check win
        if win(board, current):
            display(board)
            print("Winner is", current)
            break

        #check draw
        if draw(board):
            display(board)
            print("Draw!")
            break

        #next turn
        if current == player1:
            current = player2
        else:
            current = player1

    again = input("Play again? (yes/no): ")
    if again.upper() != "YES":
        break
