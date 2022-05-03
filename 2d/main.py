import random

length = 10
height = 7
spaces = height * length
objectAmount = spaces / 3
field = []
fieldData = {"state": "a", "neighbors": 0}


def createField():
    for i in range(spaces):
        copy = fieldData.copy()
        field.append(copy)


def generateObjects():
    global objectAmount
    while objectAmount >= 0:
        index = random.randrange(0, spaces)
        field[index]["state"] = "b"
        objectAmount -= 1


def viewField():
    currentX = 0
    msg = ""
    for i in range(spaces):
        currentX += 1
        msg += field[i]["state"]
        msg += " "
        # if current x is length, jump to next y
        if currentX % length == 0:
            msg += "\n"
            currentX = 0
    print(msg)


def checkAbove(index):
    global field, spaces
    above = index - length
    if field[above]["state"] == "b":
        field[index]["neighbors"] += 1
    print(field[index]["neighbors"])
    pass


createField()
generateObjects()
viewField()
checkAbove(19)
