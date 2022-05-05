import random


class template:
    def __init__(self):
        self.length = 10
        self.height = 7
        self.spaces = self.height * self.length
        self.objectAmount = self.spaces / 3
        self.field = []
        self.fieldData = {"state": "a", "neighbors": 0}

    def createField(self):
        for i in range(self.spaces):
            copy = self.fieldData.copy()
            self.field.append(copy)

    def generateObjects(self):
        while self.objectAmount >= 0:
            index = random.randrange(0, self.spaces)
            self.field[index]["state"] = "b"
            self.objectAmount -= 1

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


temp = template()
temp.createField()
temp.generateObjects()
temp.viewField()
