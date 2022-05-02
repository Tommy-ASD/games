import random

length = 10
height = 7
spaces = height * length
objectAmount = spaces / 3
field = []
fieldData = {"state": "a"}


def createField():
    for i in range(spaces):
        field.append(fieldData)
        print(field[i])


def generateObjects():
    global objectAmount
    # while objectAmount >= 0:
    index = random.randrange(0, spaces)
    field[1]["state"] = "b"
    for i in field:
        print(i)
    # print(field[index+1]["state"])
    # print(index)
    # objectAmount -= 1


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


createField()
generateObjects()
viewField()
