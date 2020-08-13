class Square:
    def __init__(self, x, y, btn):
        self.x = x
        self.y = y
        self.isBomb = False
        self.btn = btn
        self.number = 10
        self.flag = False

    def hasBomb(self):
        return isBomb

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def hasBomb(self):
        return self.isBomb

    def placeBomb(self):
        self.isBomb = True

    def isActive(self):
        return self.btn["state"] != "disabled"

    def toggleFlag(self, event):
        if self.isActive():
            self.flag = not self.flag
            if self.flag:
                self.btn["background"] = 'red'
            else:
                self.btn["background"] = '#AF9164'

    def checkButton(self):
        if not self.flag:
            if not self.isBomb:
                self.btn["background"] = '#424242'
                if self.number == 0:
                    self.btn['text'] = ''
                else:
                    self.btn["disabledforeground"] = '#3C91E6'
                    self.btn['text'] = self.number
            else:
                self.btn["background"] = '#FF9000'
            self.btn["font"] = '36'

            self.btn["state"] = "disabled"
