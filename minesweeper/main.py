import random


fieldState = {
    "played": False,
    "bomb": False,
    "flagged": False,
    "checkedFor0": False,
    "neighbors": 0,
    "display": "▮",
}


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
                    else:
                        i["display"] = str(i["neighbors"])
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
    tempBombs = bombs
    while tempBombs > 0:
        rand = random.randrange(0, spaces)
        if not field[rand]["bomb"] and rand != index:
            field[rand]["bomb"] = True
            tempBombs -= 1
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
    # index - length is the one exactly above. if it does not exist, do not add the space there
    if index - length >= 0:
        aboveA = True
    # same as previous, except index + length is exactly the one below
    if index + length < spaces:
        belowA = True
    # example:
    # length = 10
    # length - 1 = 9
    # if index % 10 returns 9, that means you are at the right edge of the grid
    # if index % 10 returns 0, that means you are at the left edge
    if index % length == length - 1:
        rightA = False
    if index % length == 0:
        leftA = False
    # if you remove/add length, you get the one exactly above
    above = index - length
    below = index + length
    # if you add/remove 1, you get the one to the right/left
    left = index - 1
    right = index + 1
    # same logic as previous applies here, just more than once
    aboveLeft = above - 1
    aboveRight = above + 1
    belowLeft = below - 1
    belowRight = below + 1
    # optimizable
    # use arrays?
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
    global running
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
    # input y: 10
    # output y: 9 * length
    adjustedY = (y - 1) * length
    adjustedX = x - 1
    index = adjustedX + adjustedY
    return index


while True:
    field = []
    length = int(input("Enter how wide the grid should be: "))
    height = int(input("Enter how high the grid should be: "))
    spaces = length * height
    bombs = int(
        input(
            "Enter how many bombs the grid should have (CANNOT BE GREATER THAN GRID SIZE): "
        )
    )
    flags = 0
    running = True
    generateField(
        convertToIndex(
            int(input("Pick X position: ")), int(input("Pick Y position: "))
        ),
        0,
    )
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
