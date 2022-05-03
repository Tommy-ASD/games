from dataclasses import fields
import random

field = []
xField = []
length = 10
height = 7
spaces = length * height
# O O O O O 1 1 1 O O
# O O O O O 1 B 1 O O
# O O O O 1 3 3 2 O O
# O O O O 1 B B 1 O O
# O O O O 1 2 2 1 O O
# O O O O O O O O O O
# O O O O O O O O O O


# stores information abouta space
fieldState = {
    "played": False,
    "bomb": False,
    "flagged": False,
    "x": 0,
    "y": 0,
    "neighbors": 0,
    "state": "a",
}


def playField(space):
    space = field[space]
    if space["played"]:
        return
    if space["bomb"]:
        return
    if space["flagged"]:
        return


def generateField():
    global spaces, field, fieldState
    bombs = spaces / 3

    # adds a fieldstate dictionary to all spaces
    for i in range(spaces):
        field.append(fieldState.copy())
        x = length - (i % length)
        field[i]["x"] = x
        field[i]["y"] = height - (i % height)
    while bombs > 0:
        rand = random.randrange(0, spaces)
        if not field[rand]["bomb"]:
            field[rand]["bomb"] = True
            bombs -= 1
    for i in field:
        # how to find spaces with specific X/Y positions?
        selfX = i["x"]
        selfY = i["y"]
        # checkX = length - (selfX % length)
        # check
    print(field)
    j = 0
    msg = ""
    for i in range(spaces):
        j += 1
        print(i)
        msg += field[i]["state"]
        msg += " "
        if j >= length:
            msg += "\n"
            j = 0
    print(msg)


def checkAbove(index):
    global field, spaces
    above = index - length
    below = index + length
    if field[above]["bomb"]:
        field[index]["neighbors"] += 1
    if field[below]["bomb"]:
        field[index]["neighbors"] += 1

    print(field[index]["neighbors"])
    pass


def main():

    pass


main()
generateField()
checkAbove(19)
