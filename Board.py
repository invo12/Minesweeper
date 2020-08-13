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

    def initBoard(self):
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

    def __getNumberOfFlagsInTheSurroundings(self, x, y):
        nr = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if not (j < 0 or i < 0 or i >= self.columns or j >= self.lines):
                    if self.squares[j][i].flag == True:
                        nr += 1

    def __revealSurroundings(self, x, y):
        if not (x < 0 or y < 0 or x >= self.columns or y >= self.lines):
            if self.squares[y][x].isActive() and (not self.squares[y][x].hasBomb()):
                self.squares[y][x].checkButton()
                if self.squares[y][x].number == 0:
                    self.__revealSurroundings(x - 1, y)
                    self.__revealSurroundings(x, y - 1)
                    self.__revealSurroundings(x + 1, y)
                    self.__revealSurroundings(x, y + 1)

    def __placeBombs(self):
        for i in range(self.numberOfBombs):
            x = randrange(self.columns)
            y = randrange(self.lines)
            while (self.squares[y][x].hasBomb()):
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
                if not (j < 0 or i < 0 or i >= self.columns or j >= self.lines):
                    if self.squares[j][i].hasBomb():
                        nr += 1
        return nr
