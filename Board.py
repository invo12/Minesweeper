from random import randrange


class Board:
    def __init__(self):
        self.lines = 9
        self.columns = 8
        self.numberOfBombs = 10
        self.squares = []
        for i in range(self.lines):
            self.squares.append([])
        self.lost = False
        self.win = False
        self.numberOfRevealedSquares = 0
        self.start = []

    def initBoard(self):
        self.__setStart()
        self.__placeBombs()
        self.__placeNumbers()

    def checkIfHasMine(self, x, y):
        if self.squares[y][x].number == 0:
            self.__revealSurroundings(x, y)
        else:
            self.squares[y][x].checkButton()
            if self.squares[y][x].hasBomb():
                self.lost = True
        self.numberOfRevealedSquares = 0
        for y in range(self.lines):
            for x in range(self.columns):
                if not self.squares[y][x].isActive():
                    self.numberOfRevealedSquares += 1

    def checkIfLost(self):
        return self.lost

    def checkIfWin(self):
        if self.numberOfRevealedSquares == (self.lines * self.columns - self.numberOfBombs):
            return True
        return False

    def __setStart(self):
        x = self.start[0][0]
        y = self.start[0][1]
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if self.__onBoard(i, j) and (i != x or j != y):
                    self.start.append((i, j))

    def __onBoard(self, x, y):
        return not (x < 0 or y < 0 or x >= self.columns or y >= self.lines)

    def __getNumberOfFlagsInTheSurroundings(self, x, y):
        nr = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if self.__onBoard(i, j):
                    if self.squares[j][i].flag == True:
                        nr += 1

    def __revealSurroundings(self, x, y):
        if self.__onBoard(x, y):
            if self.squares[y][x].isActive() and (not self.squares[y][x].hasBomb()):
                self.squares[y][x].checkButton()
                if self.squares[y][x].number == 0:
                    for i in range(x - 1, x + 2):
                        for j in range(y - 1, y + 2):
                            self.__revealSurroundings(i, j)

    def __placeBombs(self):
        for i in range(self.numberOfBombs):
            x = randrange(self.columns)
            y = randrange(self.lines)
            while (self.squares[y][x].hasBomb() or ((x, y) in self.start)):
                x = randrange(self.columns)
                y = randrange(self.lines)
            self.squares[y][x].placeBomb()

    def __placeNumbers(self):
        for y in range(self.lines):
            for x in range(self.columns):
                if not self.squares[y][x].hasBomb():
                    self.squares[y][x].number = self.__getNumberOfBombsInTheSurroundings(x, y)

    def __getNumberOfBombsInTheSurroundings(self, x, y):
        nr = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if self.__onBoard(i, j):
                    if self.squares[j][i].hasBomb():
                        nr += 1
        return nr
