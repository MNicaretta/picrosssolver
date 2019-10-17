from enum import Enum
import numpy as np

class Cell(Enum):
    UNKNOWN = '.'
    EMPTY = ' '
    FILL = '#'

class PicrossState():
    def __init__(self, state=None, columns=[], rows=[]):
        self.board = np.full((10,10), Cell.UNKNOWN)
        self.columns = columns
        self.rows = rows
        if state is not None:
            for i in range(len(state.columns)):
                self.columns[i] = state.columns[i]
            for i in range(len(state.rows)):
                self.rows[i] = state.rows[i]
            for r in range(len(state.board)):
                for c in range(len(state.board[r])):
                    self.board[r][c] = state.board[r][c]

    def __str__(self):
        result = ''

        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                result += self.board[r][c].value + ' '
            for i in range(len(self.rows[r])):
                result += str(self.rows[r][i]) + ' '
            result += '\n'

        has_value = True
        count = 0

        while has_value:
            has_value = False
            for i in range(len(self.columns)):
                if len(self.columns[i]) > count:
                    has_value = True
                    result += str(self.columns[i][count]) + ' '
                else:
                    result += '  '
            result += '\n'
            count += 1

        return result

def insert_obvious(state):
    row_size = len(state.board)
    column_size = len(state.board[0])

    for r in range(row_size):
        count = 0

        for i in range(len(state.rows[r])):
            count += state.rows[r][i]

        count += len(state.rows[r]) - 1

        if count == row_size:
            c = 0
            for i in range(len(state.rows[r])):
                for _ in range(state.rows[r][i]):
                    state.board[r][c] = Cell.FILL
                    c += 1

                if c < len(state.board[r]):
                    state.board[r][c] = Cell.EMPTY
                    c += 1

    for c in range(column_size):
        count = 0

        for i in range(len(state.columns[c])):
            count += state.columns[c][i]

        count += len(state.columns[c]) - 1

        if count == column_size:
            r = 0
            for i in range(len(state.columns[c])):
                for _ in range(state.columns[c][i]):
                    state.board[r][c] = Cell.FILL
                    r += 1

                if r < len(state.board):
                    state.board[r][c] = Cell.EMPTY
                    r += 1

picross = PicrossState(None,
                       [[1,1,2],   [2,1,1,1], [1,1,3], [3,3,1], [2,1,1,1], [1,2,1,1], [6,1],   [2,4],   [1,2,3,1], [1,1,1,1]],
                       [[1,1,2,2], [2,1,2],   [8],     [2,3,1], [1,1,1],   [4,1,1],   [1,1,2], [1,1,2], [4,1,1],   [1,1,1,4]])

print(picross)
insert_obvious(picross)
print(picross)
