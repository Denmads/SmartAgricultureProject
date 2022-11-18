class Parth:
    def __init__(self, x, y, fieldid=-1):
        self.x = x
        self.y = y
        self.fieldid = fieldid
        self.currentx = 0
        self.currenty = 0

    def __str__(self):
        return f"({self.fieldid}) is {self.x} by {self.y}  starts at 0,0)"

    def setxy(self,x,y):
        self.currentx = x
        self.currenty = y

    def getNextTile(self):
        if self.currentx == self.x and self.currenty == self.y:
            return [0,0]
        if self.currentx%2 == 0:
            if self.currenty == self.y:
                self.currentx = self.currentx + 1
            else:
                self.currenty += 1
        else:
            if self.currenty == 0:
                self.currentx = self.currentx + 1
            else :
                self.currenty -= 1
        return [self.currentx,self.currenty]
