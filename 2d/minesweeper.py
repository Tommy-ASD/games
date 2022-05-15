import random


fieldState = {
    "played": False,
    "bomb": False,
    "flagged": False,
    "checkedFor0": False,
    "neighbors": 0,
    "display": "▮",
}


class minesweeper:
    def __init__(self, length, width, bombs):
        self.running = True
        self.flags = 0
        self.bombs = bombs
        self.length = length
        self.height = width
        self.spaces = self.height * self.length
        self.field = []
        self.generateField(
            self.convertToIndex(
                int(input("Pick X position: ")), int(input("Pick Y position: "))
            ),
            0,
        )

    def generateField(self, index, type):

        # adds a fieldstate dictionary to all spaces
        for i in range(self.spaces):
            self.field.append(fieldState.copy())
        tempBombs = self.bombs
        while tempBombs > 0:
            rand = random.randrange(0, self.spaces)
            # if space not already bomb and not chosen index, pick space
            if not self.field[rand]["bomb"] and rand != index:
                self.field[rand]["bomb"] = True
                tempBombs -= 1
        for i in range(self.spaces):
            self.updateNeighbors(i)
        self.playField(index, type)

    def updateNeighbors(self, index):
        (
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
        ) = self.getNeighbors(index)
        self.field[index]["neighbors"] += self.field[above]["bomb"] if aboveA else 0
        self.field[index]["neighbors"] += self.field[below]["bomb"] if belowA else 0
        self.field[index]["neighbors"] += self.field[left]["bomb"] if leftA else 0
        self.field[index]["neighbors"] += self.field[right]["bomb"] if rightA else 0
        self.field[index]["neighbors"] += (
            self.field[aboveRight]["bomb"] if aboveA and rightA else 0
        )
        self.field[index]["neighbors"] += (
            self.field[aboveLeft]["bomb"] if aboveA and leftA else 0
        )
        self.field[index]["neighbors"] += (
            self.field[belowRight]["bomb"] if belowA and rightA else 0
        )
        self.field[index]["neighbors"] += (
            self.field[belowLeft]["bomb"] if belowA and leftA else 0
        )

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

    def main(self):
        self.viewField()
        self.playField(
            self.convertToIndex(
                int(input("Pick X position: ")), int(input("Pick Y position: "))
            ),
            int(input()),
        )
        self.checkWin()

    def viewField(self):
        j = 0
        msg = ""
        for i in self.field:
            j += 1
            msg += str(i["display"])
            # makes it look better
            msg += " "
            if j >= self.length:
                # if j > length, new line
                msg += "\n"
                j = 0
        print(msg)

    def playField(self, space, type):
        match type:
            # Type 0: play
            case 0:
                if self.field[space]["played"]:
                    print("Cannot play an already played space")
                    return
                if self.field[space]["flagged"]:
                    print("Cannot play a flagged space, unflag first")
                    return
                if self.field[space]["bomb"]:
                    # display all spaces
                    for i in self.field:
                        if i["bomb"] and not i["flagged"]:
                            i["display"] = "b"
                        else:
                            i["display"] = str(i["neighbors"])
                    print("fucking dumbass lmao")
                    # show space that caused loss
                    self.field[space]["display"] = "d"
                    # restart program
                    self.running = False
                else:
                    self.field[space]["display"] = str(self.field[space]["neighbors"])
                    self.field[space]["played"] = True
                    self.check0(space)
            # Type 1: flag
            case 1:
                if not self.field[space]["played"]:
                    # if a new flag added surpasses bomb amount, it won't work
                    if self.flags + 1 > self.bombs and not self.field[space]["flagged"]:
                        print("Max flags reached")
                        return
                    # flag state on/off
                    self.field[space]["flagged"] = not self.field[space]["flagged"]
                    # display on/off
                    self.field[space]["display"] = (
                        "f" if self.field[space]["flagged"] else "▮"
                    )
                    # flag count on/off
                    self.flags += 1 if self.field[space]["flagged"] else -1
                else:
                    print("Cannot flag a played space")

    def check0(self, index):
        # if i don't add if checked for 0, program will cause infinite recursion
        # the others should be relatively obvious
        if (
            self.field[index]["checkedFor0"]
            or self.field[index]["bomb"]
            or self.field[index]["flagged"]
        ):
            return
        self.field[index]["checkedFor0"] = True
        # the following has essentially the same effect as the playField() function
        # spaces checked for 0 should also count as played
        self.field[index]["played"] = True
        # displays correctly after being played
        self.field[index]["display"] = str(self.field[index]["neighbors"])
        (
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
        ) = self.getNeighbors(index)
        if self.field[index]["neighbors"] == 0:
            # if you try to do the function with a non-existing space, an error will occur
            self.check0(above) if aboveA else None
            self.check0(below) if belowA else None
            self.check0(left) if leftA else None
            self.check0(right) if rightA else None
            self.check0(aboveLeft) if aboveA and leftA else None
            self.check0(aboveRight) if aboveA and rightA else None
            self.check0(belowLeft) if belowA and leftA else None
            self.check0(belowRight) if belowA and rightA else None

    def checkWin(self):
        boolList = []
        for i in self.field:
            if i["bomb"]:
                if i["flagged"]:
                    boolList.append(True)
                else:
                    boolList.append(False)
        if all(boolList):
            print("You won")
            self.running = False


MS = minesweeper(
    int(input("Enter how wide the grid should be: ")),
    int(input("Enter how high the grid should be: ")),
    int(
        input(
            "Enter how many bombs the grid should have (CANNOT BE GREATER THAN GRID SIZE): "
        )
    ),
)
while True:
    if not MS.running:
        input("Play again? (Enter)")
        MS = minesweeper(
            int(input("Enter how wide the grid should be: ")),
            int(input("Enter how high the grid should be: ")),
            int(
                input(
                    "Enter how many bombs the grid should have (CANNOT BE GREATER THAN GRID SIZE): "
                )
            ),
        )
    try:
        MS.main()
    except ValueError:
        print("Please input a number")
