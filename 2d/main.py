import random

length = 10
height = 7
spaces = height * length
objectAmount = spaces / 3
field = []
fieldData = {"state": "a"}


def createField():
    for i in range(spaces):
        copy = fieldData.copy()
        field.append(copy)
        print(field[i])


def generateObjects():
    global objectAmount
    while objectAmount >= 0:
        index = random.randrange(0, spaces)
        field[index]["state"] = "b"
        objectAmount -= 1


def viewField():
    j = 0
    msg = ""
    for i in range(spaces):
        j += 1
        print(i)
        msg += field[i]["state"]
        if j >= length:
            msg += "\n"
            j = 0
    print(msg)


def checkAbove(index):
    global field
    space = field[index]
    x = index % length
    y = x % height
    print(x, y)
    pass


createField()
generateObjects()
viewField()
checkAbove(19)
