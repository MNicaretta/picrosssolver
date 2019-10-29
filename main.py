from enum import Enum

class CellState(Enum):
    UNKNOWN = '.'
    EMPTY = ' '
    BOX = '■'

    def __str__(self):
        return self.value

class Cell():
    def __init__(self, state=CellState.UNKNOWN):
        self.state = state

    def __str__(self):
        return self.state

class Clue():
    def __init__(self, value, filled=0):
        self.value = value
        self.filled = filled

    def isFilled(self):
        return self.remaining() == 0

    def remaining(self):
        return self.value - self.filled
    
    def __str__(self):
        return str(self.value)

class Clues():
    def __init__(self, *clues):
        self.clues = []

        for c in clues:
            self.clues.append(Clue(c))

    def fillMin(self, start, end, mark):
        space = sum(c.value + 1 for c in self.clues) - 1
        left = end - start - space

        index = 0

        for c in self.clues:
            if c.value > left:
                fill = c.value - left
                c.filled += fill
                index += c.value - fill
                for _ in range(fill):
                    mark(index, CellState.BOX)
                    index += 1
                index += 1
            else:
                index += c.value + 1

    def adjust(self, array):
        if not self.isFilled():
            for i in range(len(array)):
                start = 0
                end = 0


        if self.isFilled():
            for cell in array:
                if cell.state == CellState.UNKNOWN:
                    cell.state = CellState.EMPTY

    def isFilled(self):
        return all(c.isFilled() for c in self.clues)

class Picross():
    def __init__(self, rows=[], columns=[]):
        self.rows = rows
        self.columns = columns

        self.board = []
        for _ in range(len(self.rows)):
            array = []
            for _ in range(len(self.columns)):
                array.append(Cell())
            self.board.append(array)

    def isSolved(self):
        return all(r.isFilled() for r in self.rows)

    def set(self, r, c, state):
        self.board[r][c].state = state

    def solve(self):
        self.fillMin()
        print(self)

        while not self.isSolved():
            self.adjust()
            print(self)

    def fillMin(self):
        for r in range(len(self.rows)):
            self.rows[r].fillMin(0, len(self.columns), lambda index, state: self.set(r,index,state))

        for c in range(len(self.columns)):
            self.columns[c].fillMin(0, len(self.rows), lambda index, state: self.set(index,c,state))

    def adjust(self):
        for r in range(len(self.rows)):
            self.rows[r].adjust(self.board[r])

        for c in range(len(self.columns)):
            self.columns[c].adjust(list(map(lambda row: row[c], self.board)))

    def __str__(self):
        result = ''

        for r in range(len(self.board)):
            for cell in self.board[r]:
                result += str(cell.state) + ' '
            for clue in self.rows[r].clues:
                result += str(clue) + ' '
            result += '\n'

        has_value = True
        count = 0

        while has_value:
            has_value = False
            for clues in self.columns:
                if len(clues.clues) > count:
                    has_value = True
                    result += str(clues.clues[count]) + ' '
                else:
                    result += '  '
            result += '\n'
            count += 1

        return result

picross = Picross([Clues(1,1,1),Clues(1,1),Clues(1,2),Clues(5),Clues(1,1,1)],
                  [Clues(1,2),  Clues(3),  Clues(1,2),Clues(3),Clues(1,3)])

print(picross)
picross.solve()
