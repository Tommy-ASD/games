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
# fieldState = {
#     "played": False,
#     "bomb": False,
#     "flagged": False,
#     "neighbors": 0,
#     "state": "a",
# }
fieldState = {
    "bomb": False,
    "flagged": False,
    # state can be neighbor amount or bomb (9)
    "state": 0,
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
            field[rand]["state"] = "b"
            bombs -= 1


def viewField():
    j = 0
    msg = ""
    for i in range(spaces):
        j += 1
        print(i)
        msg += str(field[i]["state"])
        msg += " "
        if j >= length:
            msg += "\n"
            j = 0
    print(msg)


def checkAbove(index):
    global field
    above = index - length
    below = index + length
    left = index - 1
    right = index + 1
    aboveLeft = above - 1
    aboveRight = above + 1
    belowLeft = below - 1
    belowRight = below + 1
    if field[index]["state"] == "b":
        return
    neighbors = (
        field[above]["bomb"]
        + field[below]["bomb"]
        + field[left]["bomb"]
        + field[right]["bomb"]
        + field[aboveRight]["bomb"]
        + field[aboveLeft]["bomb"]
        + field[belowRight]["bomb"]
        + field[belowLeft]["bomb"]
    )
    field[index]["state"] += neighbors

    print(field[index]["state"])


def main():

    pass


main()
generateField()
checkAbove(15)
viewField()
