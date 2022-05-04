import random

field = []
xField = []
length = 10
height = 7
spaces = length * height

fieldState = {
    "played": False,
    "bomb": False,
    "flagged": False,
    "neighbors": 0,
    # display can be neighbor amount, bomb (b) or flagged (f)
    "display": "▮",
}

# TODO: make it possible to play using X/Y positions and more stuff
def playField(space, type):

    match type:
        # Type 0: play
        case 0:
            if field[space]["played"]:
                return 0
            if field[space]["flagged"]:
                return 1
            if field[space]["bomb"]:
                for i in field:
                    if i["bomb"]:
                        i["display"] = "b"
            else:
                field[space]["display"] = str(field[space]["neighbors"])
                field[space]["played"] = True
        # Type 1: flag
        case 1:
            if not field[space]["played"]:
                field[space]["flagged"] = not field[space]["flagged"]
                field[space]["display"] = "f" if field[space]["flagged"] else "▮"


def generateField():
    global spaces, field, fieldState
    bombs = spaces / 3

    # adds a fieldstate dictionary to all spaces
    for i in range(spaces):
        field.append(fieldState.copy())
    while bombs > 0:
        rand = random.randrange(0, spaces)
        if not field[rand]["bomb"]:
            field[rand]["bomb"] = True
            bombs -= 1


def viewField():
    j = 0
    msg = ""
    for i in range(spaces):
        j += 1
        msg += str(field[i]["display"])
        msg += " "
        if j >= length:
            msg += "\n"
            j = 0
    print(msg)


def checkHorizontal(index):
    global field, spaces
    if field[index]["display"] == "b":
        return
    # Direction available
    aboveA = False
    belowA = False
    if index - length > 0:
        aboveA = True
    if index + length < spaces:
        belowA = True
    above = index - length
    below = index + length
    field[index]["neighbors"] += field[above]["bomb"] if aboveA else 0
    field[index]["neighbors"] += field[below]["bomb"] if belowA else 0
    leftA = True
    rightA = True
    if index % length == length - 1:
        rightA = False
    if index % length == 0:
        leftA = False
    left = index - 1
    right = index + 1
    field[index]["neighbors"] += field[left]["bomb"] if leftA else 0
    field[index]["neighbors"] += field[right]["bomb"] if rightA else 0
    aboveLeft = above - 1
    aboveRight = above + 1
    belowLeft = below - 1
    belowRight = below + 1
    field[index]["neighbors"] += field[aboveRight]["bomb"] if aboveA and rightA else 0
    field[index]["neighbors"] += field[aboveLeft]["bomb"] if aboveA and leftA else 0
    field[index]["neighbors"] += field[belowRight]["bomb"] if belowA and rightA else 0
    field[index]["neighbors"] += field[belowLeft]["bomb"] if belowA and leftA else 0


def main():

    pass


main()
generateField()
for i in range(spaces):
    checkHorizontal(i)
while True:
    viewField()
    playField(int(input()), int(input()))
