import re
import sys

board = [[0 for i in range(3)] for j in range(3)]
round = 1
finished = False
validMove = False

def main():
    game()

def initialize_board():
    global board
    for r in range(3):
        for c in range(3):
            board[r][c] = "[ ]"

def display():
    global finished, board
    if not finished:
        print(f"Round {round}:")
    else:
        print("GAME COMPLETE!")
    for r in range(len(board)):
        for c in range(len(board[0])):
            print(board[r][c], end="")
        print()

def prompt_input():
    global finished, round
    if not finished:
        if round % 2 == 1:
            print("X, make your move (row,col) : ")
        else:
            print("O, make your move (row,col) : ")
    else:
        print("Play again? Y/N ")

def place_pieces(str):
    global validMove, board, round
    if matches := re.search(r"^([0-2]),([0-2])$", str):
        try:
            row, column = matches.groups()
            row = int(row)
            column = int(column)
        except ValueError:
            validMove = False
            return
    else:
        validMove = False
        print("Enter valid input")
        return
    for r in range(len(board)):
        if r == row:
            for c in range(len(board[0])):
                if c == column:
                    if round % 2 == 1:
                        if board[r][c] == "[ ]":
                            board[r][c] = "[X]"
                            round += 1
                            validMove = True
                        else:
                            validMove = False
                    else:
                        if board[r][c] == "[ ]":
                            board[r][c] = "[O]"
                            round += 1
                            validMove = True
                        else:
                            validMove = False

def check_finished():
    global board, round, finished
    if round >= 10:
        finished = True
        return
    for r in range(len(board)):
        if not board[r][0] == "[ ]" and board[r][0] == board[r][1] and board[r][1] == board[r][2]:
            finished = True
    for c in range(len(board[0])):
        if not board[0][c] == "[ ]" and board[0][c] == board[1][c] and board[1][c] == board[2][c]:
            finished = True
    if not board[0][0] == "[ ]" and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        finished = True
    if not board[0][2] == "[ ]" and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        finished = True


def reset():
    global round, finished, validMove
    round = 1
    finished = False
    validMove = False
    initialize_board()

def play():
    display()
    prompt_input()
    try:
        place_pieces(input())
    except EOFError:
        sys.exit()
    check_finished()

def game():
    global validMove, round, finished
    inputMove = ""
    reset()
    while True:
        while not finished:
            play()
        if finished:
            display()
            while True:
                try:
                    prompt_input()
                    inputMove = input()
                except EOFError:
                    sys.exit()
                else:
                    inputMove = inputMove.lower().strip()
                    if matches := re.search(r"^([yn])$", inputMove):
                        if matches.group(1) == "y":
                            reset()
                            break
                        else:
                            sys.exit()
                    else:
                        print("Enter valid input")


if __name__ == "__main__":
    main()
