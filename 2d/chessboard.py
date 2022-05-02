import random

length = 8
height = 8
spaces = height * length
field = []
fieldData = {"state": "a"}


def createField():
    for i in range(spaces):
        copy = fieldData.copy()
        field.append(copy)
        print(field[i])


def viewField():
    j = 0
    msg = " "
    for i in range(length):
        msg += str(i + 1)
        msg += " "
    msg += "\n"
    for i in range(spaces):
        loop = 0
        j += 1
        if j >= length:
            msg += "\n"
            loop += 1
            msg += str(loop)
            j = 0
        print(i)
        msg += " "
        msg += field[i]["state"]
    print(msg)


def checkAbove(index):
    global field
    space = field[index]

    pass


createField()
viewField()
