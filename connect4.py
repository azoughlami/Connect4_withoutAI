# https://www.youtube.com/watch?v=UYgyRArKDEs
import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board = np.zeros(shape := (ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
    return None


def print_board(board):
    print(np.flip(board,0))

def winning_move(board, piece):
    #check horizontal location
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and \
               board[r][c+2] == piece and board[r][c + 3]:
               return True

    # check vertical location
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and \
               board[r+2][c] == piece and board[r+3][c]:
               return True

    # check positively sloaped diag
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c+1] == piece and \
                    board[r + 2][c+2] == piece and board[r + 3][c+3]:
                return True

    # check negatively sloaped diag
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and \
                    board[r - 2][c + 2] == piece and board[r - 3][c + 3]:
                return True

    return None



def main():
    board = create_board()
    print_board(board)
    print()
    # print(board[5][3:5])

    game_over = False
    turn = 0

    while not game_over:
        # player 1 input
        if turn == 0:
            col = int(input("player 1 make your col (0-6):"))

            if is_valid_location(board,col):
                row = get_next_open_row(board,col)
                drop_piece(board,row, col, 1)

                if winning_move(board, 1):
                    print("PLAYER 1 WINS!")
                    game_over = True



        # player 2 2 input
        else:
            col = int(input("player 2 make your col (0-6):"))
            print(col)
            if is_valid_location(board,col):
                row = get_next_open_row(board,col)
                drop_piece(board,row, col,2)

                if winning_move(board, 2):
                    print("PLAYER  2 WINS!")
                    game_over = True

        print_board(board)

        turn += 1

        turn = turn % 2


if __name__ == '__main__':
    main()
