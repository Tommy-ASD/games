import random


class template:
    def __init__(self):
        self.length = 8
        self.height = 8
        self.spaces = self.height * self.length
        self.objectAmount = self.spaces / 3
        self.field = []
        self.fieldData = {"state": ".", "neighbors": 0}
        # piece types:
        # p: Pawn
        # b: Bishop
        # k: Knight
        # r: Rook
        # q: Queen
        # c: King
        self.piece = {"positon": 0, "color": False, "moved": False, "type": "p"}
        self.blackPieces = []
        self.whitePieces = []

    def createField(self):
        for i in range(self.spaces):
            copy = self.fieldData.copy()
            self.field.append(copy)

    def generateWhite(self):
        for i in range(16):
            self.whitePieces.append(self.piece)
        self.field[0]["state"] = "t"
        self.field[1]["state"] = "h"
        self.field[2]["state"] = "b"
        self.field[3]["state"] = "k"
        self.field[4]["state"] = "q"
        self.field[5]["state"] = "b"
        self.field[6]["state"] = "h"
        self.field[7]["state"] = "t"
        # generate pawns
        for i in range(self.length):
            index = self.length + i
            self.field[index]["state"] = "p"
            pass

    def generateBlack(self):
        self.field[56]["state"] = "t"
        self.field[57]["state"] = "h"
        self.field[58]["state"] = "b"
        self.field[59]["state"] = "k"
        self.field[60]["state"] = "q"
        self.field[61]["state"] = "b"
        self.field[62]["state"] = "h"
        self.field[63]["state"] = "t"
        # generate pawns
        for i in range(self.length):
            # it just works
            index = self.length * self.length - self.length - i - 1
            self.field[index]["state"] = "p"
            pass

    def viewField(self):
        currentX = 0
        msg = ""
        for i in self.field:
            currentX += 1
            msg += i["state"]
            msg += " "
            # if current x is length, jump to next y
            if currentX % self.length == 0:
                msg += "\n"
                currentX = 0
        print(msg)

    def getNeighbors(self, index):
        if self.field[index]["display"] == "b":
            return
        # Direction available
        aboveA = False
        belowA = False
        leftA = True
        rightA = True
        # index - length is the one exactly above. if it does not exist, do not add the space there
        if index - self.length >= 0:
            aboveA = True
        # same as previous, except index + length is exactly the one below
        if index + self.length < self.spaces:
            belowA = True
        # example:
        # length = 10
        # length - 1 = 9
        # if index % 10 returns 9, that means you are at the right edge of the grid
        # if index % 10 returns 0, that means you are at the left edge
        if index % self.length == self.length - 1:
            rightA = False
        if index % self.length == 0:
            leftA = False
        # if you remove/add length, you get the one exactly above
        above = index - self.length
        below = index + self.length
        # if you add/remove 1, you get the one to the right/left
        left = index - 1
        right = index + 1
        # same logic as previous applies here, just more than once
        aboveLeft = above - 1
        aboveRight = above + 1
        belowLeft = below - 1
        belowRight = below + 1
        # optimizable
        # use arrays?
        return (
            above,
            below,
            left,
            right,
            aboveLeft,
            aboveRight,
            belowLeft,
            belowRight,
            aboveA,
            belowA,
            leftA,
            rightA,
        )

    def convertToIndex(self, x, y):
        # input y: 10
        # output y: 9 * length
        adjustedY = (y - 1) * self.length
        adjustedX = x - 1
        index = adjustedX + adjustedY
        return index


temp = template()
temp.createField()
temp.generateObjects()
temp.generateWhite()
temp.generateBlack()
temp.viewField()
