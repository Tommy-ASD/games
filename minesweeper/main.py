import random

field = []
xField = []
length = 10
height = 7
flags = 0
spaces = length * height
bombs = spaces / 5
running = True

fieldState = {
    "played": False,
    "bomb": False,
    "flagged": False,
    "checkedFor0": False,
    "neighbors": 0,
    # display can be neighbor amount, bomb (b) or flagged (f)
    "display": "▮",
}

# TODO: make it possible to play using X/Y positions and more stuff
def playField(space, type):
    global running, flags, bombs
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
                check0(space)
        # Type 1: flag
        case 1:
            if not field[space]["played"]:
                if flags + 1 > bombs and not field[space]["flagged"]:
                    print("Max flags reached")
                    return
                field[space]["flagged"] = not field[space]["flagged"]
                field[space]["display"] = "f" if field[space]["flagged"] else "▮"
                flags += 1 if field[space]["flagged"] else -1
            else:
                print("Cannot flag a played space")


def generateField(index, type):
    global spaces, field, fieldState, bombs

    # adds a fieldstate dictionary to all spaces
    for i in range(spaces):
        field.append(fieldState.copy())
    while bombs > 0:
        rand = random.randrange(0, spaces)
        if not field[rand]["bomb"] and rand != index:
            field[rand]["bomb"] = True
            bombs -= 1
    for i in range(spaces):
        updateNeighbors(i)
    playField(index, type)


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


def getNeighbors(index):
    global field, spaces
    if field[index]["display"] == "b":
        return
    # Direction available
    aboveA = False
    belowA = False
    leftA = True
    rightA = True
    if index - length >= 0:
        aboveA = True
    if index + length < spaces:
        belowA = True
    if index % length == length - 1:
        rightA = False
    if index % length == 0:
        leftA = False
    above = index - length
    below = index + length
    left = index - 1
    right = index + 1
    aboveLeft = above - 1
    aboveRight = above + 1
    belowLeft = below - 1
    belowRight = below + 1
    return (
        above,
        below,
        left,
        right,
        aboveLeft,
        aboveRight,
        belowLeft,
        belowRight,
        aboveA,
        belowA,
        leftA,
        rightA,
    )


def updateNeighbors(index):
    (
        above,
        below,
        left,
        right,
        aboveLeft,
        aboveRight,
        belowLeft,
        belowRight,
        aboveA,
        belowA,
        leftA,
        rightA,
    ) = getNeighbors(index)
    field[index]["neighbors"] += field[above]["bomb"] if aboveA else 0
    field[index]["neighbors"] += field[below]["bomb"] if belowA else 0
    field[index]["neighbors"] += field[left]["bomb"] if leftA else 0
    field[index]["neighbors"] += field[right]["bomb"] if rightA else 0
    field[index]["neighbors"] += field[aboveRight]["bomb"] if aboveA and rightA else 0
    field[index]["neighbors"] += field[aboveLeft]["bomb"] if aboveA and leftA else 0
    field[index]["neighbors"] += field[belowRight]["bomb"] if belowA and rightA else 0
    field[index]["neighbors"] += field[belowLeft]["bomb"] if belowA and leftA else 0


def check0(index):
    if field[index]["checkedFor0"] or field[index]["bomb"] or field[index]["flagged"]:
        return
    field[index]["checkedFor0"] = True
    field[index]["played"] = True
    field[index]["display"] = str(field[index]["neighbors"])
    (
        above,
        below,
        left,
        right,
        aboveLeft,
        aboveRight,
        belowLeft,
        belowRight,
        aboveA,
        belowA,
        leftA,
        rightA,
    ) = getNeighbors(index)
    if field[index]["neighbors"] == 0:
        check0(above) if aboveA else None
        check0(below) if belowA else None
        check0(left) if leftA else None
        check0(right) if rightA else None
        check0(aboveLeft) if aboveA and leftA else None
        check0(aboveRight) if aboveA and rightA else None
        check0(belowLeft) if belowA and leftA else None
        check0(belowRight) if belowA and rightA else None


def checkWin():
    boolList = []
    for i in field:
        if i["bomb"]:
            if i["flagged"]:
                boolList.append(True)
            else:
                boolList.append(False)
            if all(boolList):
                print("You won")
                running = False


def convertToIndex(x, y):
    adjustedY = (y - 1) * length
    adjustedX = x - 1
    index = adjustedX + adjustedY
    return index


generateField(
    convertToIndex(int(input("Pick X position: ")), int(input("Pick Y position: "))), 0
)


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
        checkWin()
    input("Play again? (Enter)")
    generateField(
        convertToIndex(
            int(input("Pick X position: ")), int(input("Pick Y position: "))
        ),
        0,
    )
    running = True
