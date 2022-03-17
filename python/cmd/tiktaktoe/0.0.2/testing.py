from copyreg import constructor


gameState = []
currentPlayer = False


def printGameState(_gameState):
    gameState = _gameState
    print(gameState[0][0])
    print(gameState[0][1])
    print(gameState[0][2])


def checkForWin(_gameState):
    gameState = _gameState
    print(gameState[1])
    for i in range(len(gameState[1])):
        if all(gameState[1][i]):
            print("player 2 won")
        elif not any(gameState[1][i]):
            print("player 1 won")

        for j in range(len(gameState[1][i])):
            print(f"gameState[1][{i}][{j}]: {gameState[1][i][j]}")


def changeGameState(_gameState, _playerSymbols):
    change = []
    # i want to find a way to make these written in one input
    change.append(int(input("What X position do you want to play? : ")) - 1)
    change.append(int(input("What Y position do you want to play? : ")) - 1)
    global currentPlayer
    gameState = _gameState
    playerSymbols = _playerSymbols
    if gameState[1][change[0]][change[1]] == None:
        gameState[0][change[0]][change[1]] = playerSymbols[currentPlayer]
        gameState[1][change[0]][change[1]] = currentPlayer
        currentPlayer = not currentPlayer
        print(currentPlayer)
    else:
        # restart function if failed
        print("Cell has already been played")
        changeGameState(gameState, playerSymbols)


def newRound(_gameState, _playerSymbols):
    gameState = _gameState
    playerSymbols = _playerSymbols
    printGameState(gameState)
    print(f"Player {int(currentPlayer)+1}, make your move")
    # check bool array for whether cell has been taken
    changeGameState(gameState, playerSymbols)


def game(_beginningGameState, _playerSymbols):
    playerSymbols = _playerSymbols
    currentGameState = _beginningGameState
    while True:
        print(
            f"Current Game State: {currentGameState}, Current Player: {currentPlayer}"
        )
        newRound(currentGameState, playerSymbols)
        checkForWin(currentGameState)


def setup():
    # basic setup
    emptySymbol = input("what symbol should an empty cell have?\n")
    playerSymbols = []
    playerSymbols.append(input("what symbol should player 1 have?\n"))
    playerSymbols.append(input("what symbol should player 2 have?\n"))
    print(playerSymbols)
    # player is displayed as a boolean
    # False is player 1, True is player 2
    # plan: have gamestate be stored in 2d array
    # played cells will be stored in separate array, this makes stuff easier

    beginningGameState = [
        [
            [emptySymbol, emptySymbol, emptySymbol],
            [emptySymbol, emptySymbol, emptySymbol],
            [emptySymbol, emptySymbol, emptySymbol],
        ],
        [[None, None, None], [None, None, None], [None, None, None]],
    ]
    game(beginningGameState, playerSymbols)


def main():
    setup()


main()
