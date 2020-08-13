from tkinter import *
from Square import Square
from functools import partial
from Board import Board
from threading import Thread
import time

def initGraphics(board, root):
    root.geometry(str(windowWidth) + 'x' + str(windowHeight))
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws / 2) - (windowWidth / 2)
    y = (hs / 2) - (windowHeight / 2)
    root.geometry('%dx%d+%d+%d' % (windowWidth, windowHeight, x, y))
    frame = Frame(root)
    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)
    frame.grid(row=0, column=0, sticky=N + S + E + W)
    grid = Frame(frame)
    grid.grid(sticky=N + S + E + W, column=0, row=7, columnspan=5)
    Grid.rowconfigure(frame, 7, weight=1)
    Grid.columnconfigure(frame, 0, weight=1)

    # example values
    for x in range(board.columns):
        for y in range(board.lines):
            f = partial(startGame, x, y)
            btn = Button(frame, fg='blue', command=f, width=1, height=1)
            btn['activebackground'] = '#AC8C5D'
            btn['background'] = '#AF9164'
            btn.grid(column=x, row=y, sticky=N + S + E + W)
            board.squares[y].append(Square(y, x, btn))
            g = partial(board.squares[y][x].toggleFlag)
            btn.bind("<Button-3>", g)
    for x in range(board.columns):
        Grid.columnconfigure(frame, x, weight=1)

    for y in range(board.lines):
        Grid.rowconfigure(frame, y, weight=1)

    return frame
def startGame(a, b):
    for x in range(board.columns):
        for y in range(board.lines):
            f = partial(board.checkIfHasMine, x, y)
            board.squares[y][x].btn["command"] = f
    board.start = [(a, b)]
    board.initBoard()
    board.checkIfHasMine(a, b)


def checkIfGameIsOver(board, root, frame):
    while 1:
        if board.checkIfWin():
            popup_bonus("You Won!")
            break
        elif board.checkIfLost():
            popup_bonus("You Lost!")
            break
        time.sleep(1)
    frame.destroy()

def popup_bonus(name):
    win = Toplevel()
    win.protocol('WM_DELETE_WINDOW', root.destroy)
    win.wm_title("")

    l = Label(win, text=name)
    l.grid(row=0, column=0)

    b = Button(win, text="Okay", command=root.destroy)
    b.grid(row=1, column=0)


if __name__ == '__main__':
    windowWidth = 400
    windowHeight = 600
    board = Board()
    root = Tk()

    frame = initGraphics(board, root)
    t = Thread(target=checkIfGameIsOver, args=[board, root, frame, ])
    t.daemon = True
    t.start()
    root.mainloop()
