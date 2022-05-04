from lib2to3.pytree import convert
import random

field = []
xField = []
length = 10
height = 7
spaces = length * height
running = True

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
    global running
    match type:
        # Type 0: play
        case 0:
            if field[space]["played"]:
                print("Cannot play an already played space")
                return
            if field[space]["flagged"]:
                print("Cannot play a flagged space, unflag first")
                return
            if field[space]["bomb"]:
                for i in field:
                    if i["bomb"]:
                        i["display"] = "b"
                print("fucking dumbass lmao")
                field[space]["display"] = "d"
                running = False
                return
            else:
                field[space]["display"] = str(field[space]["neighbors"])
                field[space]["played"] = True
        # Type 1: flag
        case 1:
            if not field[space]["played"]:
                field[space]["flagged"] = not field[space]["flagged"]
                field[space]["display"] = "f" if field[space]["flagged"] else "▮"
            else:
                print("Cannot flag a played space")


def generateField():
    global spaces, field, fieldState
    bombs = spaces / 5

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


def check(index):
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


def convertToIndex(x, y):
    adjustedY = (y - 1) * length
    adjustedX = x - 1
    index = adjustedX + adjustedY
    print(index)
    return index


generateField()
for i in range(spaces):
    check(i)


while True:
    viewField()
    while running:
        playField(
            convertToIndex(
                int(input("Pick X position: ")), int(input("Pick Y position: "))
            ),
            int(input()),
        )
        viewField()
    generateField()
    input("Play again? (Enter)")
    running = True
