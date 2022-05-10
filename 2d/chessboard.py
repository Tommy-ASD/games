import random


class template:
    def __init__(self):
        self.length = 8
        self.height = 8
        self.spaces = self.height * self.length
        self.objectAmount = self.spaces / 3
        self.field = []
        self.fieldData = {"state": ".", "piece": None}
        # piece types:
        # p: Pawn
        # b: Bishop
        # k: Knight
        # r: Rook
        # q: Queen
        # c: King
        self.piece = {"position": 0, "color": False, "moved": False, "type": "p"}
        self.pieces = []

    def createField(self):
        for i in range(self.spaces):
            copy = self.fieldData.copy()
            self.field.append(copy)

    def generateWhite(self):
        for i in range(16):
            self.pieces.append(self.piece.copy())
            self.pieces[i]["color"] = True
            self.pieces[i]["position"] = i
            self.field[self.pieces[i]["position"]]["piece"] = i

        self.pieces[0]["type"] = "t"
        self.pieces[1]["type"] = "k"
        self.pieces[2]["type"] = "b"
        self.pieces[3]["type"] = "c"
        self.pieces[4]["type"] = "q"
        self.pieces[5]["type"] = "b"
        self.pieces[6]["type"] = "k"
        self.pieces[7]["type"] = "t"

    def generateBlack(self):
        pass
        for i in range(16):
            self.pieces.append(self.piece.copy())
            self.pieces[i + 16]["color"] = True
            self.pieces[i + 16]["position"] = self.spaces - i - 1
            self.field[self.pieces[i + 16]["position"]]["piece"] = i + 16

        self.pieces[0 + 16]["type"] = "t"
        self.pieces[1 + 16]["type"] = "k"
        self.pieces[2 + 16]["type"] = "b"
        self.pieces[3 + 16]["type"] = "q"
        self.pieces[4 + 16]["type"] = "c"
        self.pieces[5 + 16]["type"] = "b"
        self.pieces[6 + 16]["type"] = "k"
        self.pieces[7 + 16]["type"] = "t"

    def viewField(self):
        currentX = 0
        msg = ""
        for i in self.pieces:
            self.field[i["position"]]["state"] = i["type"]
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

    def play(self, positionFrom, positionTo):
        if self.field[positionFrom]["piece"] is None:
            print("that isn't a piece")
            return
        allowedMovement = self.checkAllowedMovement(
            self.pieces[self.field[positionFrom]["piece"]]
        )
        if positionTo not in allowedMovement:
            print("not allowed")
            return
        self.pieces[self.field[positionFrom]["piece"]]["position"] = positionTo
        self.pieces[self.field[positionFrom]["piece"]]["moved"] = True
        self.field[positionTo]["piece"] = self.field[positionFrom]["piece"]
        self.field[positionFrom]["piece"] = None

    def checkAllowedMovement(self, piece):
        movement = []
        allowedMovement = []
        match piece["type"]:
            case "p":
                if piece["color"]:
                    movement.append(self.length)
                else:
                    movement.append(-self.length)
                if not piece["moved"]:
                    movement.append(movement[0] * 2)
                for i in movement:
                    if self.field[piece["position"] + i]["piece"] == None:
                        allowedMovement.append(piece["position"] + i)
                    if self.field[piece["position"] + i + 1]["piece"] != None:
                        allowedMovement.append(piece["position"] + i + 1)
                    if self.field[piece["position"] + i - 1]["piece"] != None:
                        allowedMovement.append(piece["position"] + i - 1)
            case "t":

                pass
            case "k":
                pass
            case "b":
                pass
            case "q":
                pass
            case "c":
                pass
        return allowedMovement


temp = template()
temp.createField()
temp.generateWhite()
temp.generateBlack()
temp.play(temp.convertToIndex(1, 2), temp.convertToIndex(1, 4))
temp.viewField()
