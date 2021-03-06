class template:
    def __init__(self):
        self.player = False
        self.length = 3
        self.spaces = self.length**2
        self.field = []
        self.fieldData = {"state": "▮"}
        self.running = True

    def createField(self):
        for i in range(self.spaces):
            copy = self.fieldData.copy()
            self.field.append(copy)

    def viewField(self):
        currentX = 0
        msg = ""
        for i in range(self.spaces):
            currentX += 1
            msg += self.field[i]["state"]
            msg += " "
            # if current x is length, jump to next y
            if currentX % self.length == 0:
                msg += "\n"
                currentX = 0
        print(msg)

    def playField(self, index):
        if self.field[index]["state"] == "▮":
            self.field[index]["state"] = "O" if self.player else "X"
            self.player = not self.player
        else:
            print("That index is already played")

    def convertToIndex(self, x, y):
        # input y: 10
        # output y: 9 * length
        adjustedY = (y - 1) * self.length
        adjustedX = x - 1
        index = adjustedX + adjustedY
        return index

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

    def getBelow(self, index):
        # adding length gives index directly below
        below = index + self.length
        # if there is no line below
        if not index + self.length < self.spaces:
            print(f"{self.field[index]['state']} won")
            return True
        # only proceed if next index is played by same player
        if (
            self.field[below]["state"] == self.field[index]["state"]
            and self.field[index]["state"] != "▮"
        ):
            return self.getBelow(below)

    def getRight(self, index):
        right = index + 1
        # if index is at the very right side of the screen
        # this function always starts at the very left side
        if right % self.length == 0:
            print(f"{self.field[index]['state']} won")
            return True
        # only proceed if next index is played by same player
        if (
            self.field[right]["state"] == self.field[index]["state"]
            and self.field[index]["state"] != "▮"
        ):
            return self.getRight(right)

    def getBottomRight(self, index):
        # if index is bottom-right of grid
        if index == self.length**2 - 1:
            print(f"{self.field[index]['state']} won")
            return True
        # bottom-right of current index's position
        bottomRight = (index + self.length) + 1
        # only proceed if next index is played by same player
        if (
            self.field[bottomRight]["state"] == self.field[index]["state"]
            and self.field[index]["state"] != "▮"
        ):
            return self.getBottomRight(bottomRight)

    def getTopRight(self, index):
        # if index is top-right of grid
        if index == self.length - 1:
            print(f"{self.field[index]['state']} won")
            return True
        # top-right of current index's position
        topRight = (index - self.length) + 1
        # only proceed if next index is played by same player
        if (
            self.field[topRight]["state"] == self.field[index]["state"]
            and self.field[index]["state"] != "▮"
        ):
            return self.getTopRight(topRight)

        pass

    def checkWins(self):
        # check all rows/coloums for win
        # can be optimized to only check those that apply to last played index
        boolList = []
        for i in range(self.length):
            boolList.append(self.getBelow(i))
            boolList.append(self.getRight(self.length * i))
        # @PARAM (self.length**2 + 1) is the index after the last one
        # - self.length is to get the top-right
        boolList.append(self.getTopRight((self.length**2) - self.length))
        boolList.append(self.getBottomRight(0))
        if any(boolList):
            self.running = False

    # check top-left bottom-right
    def checkTRBL(self, index):
        # check all directions for win
        # can be optimized to only check those that apply to last played index
        topLeft = index - (self.length - 1)
        bottomRight = index + (self.length + 1)
        boolList = []
        boolList.append(self.getBelow(index))
        boolList.append(self.getRight(index))
        boolList.append(self.getBottomRight(index))
        boolList.append(self.getTopRight(index))
        if any(boolList):
            self.running = False


while True:
    input("Press enter to continue: ")
    temp = template()
    temp.createField()
    while temp.running:
        temp.playField(
            temp.convertToIndex(
                int(input("Enter X coords: ")), int(input("Enter Y coords: "))
            )
        )
        temp.viewField()
        temp.checkWins()
    temp.checkWins()
