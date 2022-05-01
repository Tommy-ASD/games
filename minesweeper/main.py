from dataclasses import fields
import random

field = []
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
    for i in spaces:
        field.append(fieldState)
        field[i]["x"] = length - (i % length)
        field[i]["y"] = height - (i % height)
    while bombs > 0:
        rand = random.randrange(0, spaces)
        if not field[rand]["bomb"]:
            field[rand]["bomb"] = True
            bombs -= 1
    for i in field:
        selfX = i["x"]
        selfY = i["y"]


def main():

    pass


main()
