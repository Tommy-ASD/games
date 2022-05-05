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

    def checkAbove(self, index):
        above = index - self.length
        if self.field[above]["state"] == "b":
            self.field[index]["neighbors"] += 1
        print(self.field[index]["neighbors"])
        pass


temp = template()
temp.createField()
temp.generateObjects()
temp.viewField()
temp.checkAbove(19)
