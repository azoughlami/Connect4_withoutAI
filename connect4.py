# https://www.youtube.com/watch?v=UYgyRArKDEs
import numpy as np


def main():
    board = create_board()
    print(board)

    game_over = False
    turn = 0

    while not game_over:
        #player 1 input
        if turn == 0:
            selection = int(input("player 1 make your selection (0-6):"))
            print(selection)
        # palyr 2 input
        else:
            selection = int(input("player 2 make your selection (0-6):"))
            print(selection)
        turn += 1

        turn = turn % 2








def create_board():
    board = np.zeros(shape:= (6,7))
    return board




















if __name__ == '__main__':
    main()
