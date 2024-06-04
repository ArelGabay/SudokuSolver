def is_valid(row, column, board):
    num = board[row][column]
    # checking if row is valid. #
    for i in range(9):
        if i == column:
            pass
        elif board[row][i] == num:
            return False

    # checking if column is valid. #
    for i in range(9):
        if i == row:
            pass
        elif board[i][column] == num:
            return False

    # checking if box is valid. #
    start_box_r = (row // 3) * 3  # finding top left corner row #
    start_box_c = (column // 3) * 3  # finding top left corner column #

    for i in range(start_box_r, start_box_r + 3):
        for j in range(start_box_c, start_box_c + 3):
            if i == row and j == column:
                pass
            elif board[i][j] == num:
                return False
    return True


def find_zero(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return 10, 10


def solve(board):
    i, j = find_zero(board)

    if i == 10:
        return True

    else:
        for num in range(1, 10):
            board[i][j] = num
            if is_valid(i, j, board):
                if solve(board):
                    return True
            else:
                board[i][j] = 0

        board[i][j] = 0
        return False


def print_board(board):
    for i in range(9):
        print(board[i])
