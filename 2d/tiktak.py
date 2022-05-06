class template:
    def __init__(self, size):
        self.player = False
        self.length = size
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
        for i in self.field:
            currentX += 1
            msg += i["state"]
            msg += " "
            # if current x is length, jump to next y
            if currentX % self.length == 0:
                msg += "\n"
                currentX = 0
        print(msg)

    def playField(self, x, y):
        adjustedX = x - 1
        adjustedY = (y - 1) * self.length
        index = adjustedX + adjustedY
        if self.field[index]["state"] == "▮":
            self.field[index]["state"] = "O" if self.player else "X"
            self.player = not self.player
        else:
            print("That index is already played")
        temp.viewField()
        temp.checkWins(adjustedX, adjustedY)

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
        # why broken
        # what
        right = index + 1
        # if index is at the very right side of the grid
        # this function always starts at the very left side
        # self.length is at the very left side
        if right % self.length == 0:
            print(f"{self.field[index]['state']} won")
            return True
        # only proceed if next index is played by same player
        if (
            self.field[right]["state"] == self.field[index]["state"]
            and self.field[index]["state"] != "▮"
        ):
            # repeat function until the very right side of the grid
            return self.getRight(right)

    def getBottomRight(self, index):
        # if index is bottom-right of grid
        if index == self.length**2 - 1:
            print(f"{self.field[index]['state']} won")
            # return True
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

    def checkWins(self, x, y):
        # check all rows/coloums for win
        # can be optimized to only check those that apply to last played index
        boolList = []
        boolList.append(self.getBelow(x))
        boolList.append(self.getRight(y))
        # @PARAM (self.length**2 + 1) is the index after the last one
        # - self.length is to get the top-right
        boolList.append(self.getTopRight((self.length**2) - self.length))
        boolList.append(self.getBottomRight(0))
        if any(boolList):
            self.running = False


while True:
    input("Press enter to continue: ")
    temp = template(int(input("How large should the grid be?\n")))
    temp.createField()
    while temp.running:
        temp.playField(int(input("Enter X coords: ")), int(input("Enter Y coords: ")))
