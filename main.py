from enum import Enum
import numpy as np

class Cell(Enum):
    UNKNOWN = '.'
    EMPTY = 'X'
    FILL = '#'

columns = [[1,2], [1,2],   [1,5],   [2,3,2], [3,3],   [2,2,1], [3,2], [1,6],   [2,1,2,1], [4,2]]
rows =    [[1],   [1,1,2], [2,2,1], [2,1],   [1,3,4], [2,2,1], [1,6], [3,2,2], [5,2,1],   [1,5]]

board = np.full((10,10), Cell.UNKNOWN)

def print_board():
    global board
    global columns
    global rows

    for r in range(len(board)):
        for c in range(len(board[r])):
            print(board[r][c].value, end=' ')
        for i in range(len(rows[r])):
            print(rows[r][i], end=' ')
        print('')

    has_value = True
    count = 0

    while has_value:
        has_value = False
        for i in range(len(columns)):
            if len(columns[i]) > count:
                has_value = True
                print(columns[i][count], end=' ')
            else:
                print(' ', end=' ')
        print('')
        count += 1

print_board()