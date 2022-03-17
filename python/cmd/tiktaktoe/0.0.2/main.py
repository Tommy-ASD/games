from copyreg import constructor


gameState = []


def printGameState(_gameState):
    gameState = _gameState
    print(gameState[0])
    print(gameState[1])
    print(gameState[2])


def newRound(_gameState, _playerSymbols, _currentPlayer, _playedCells):
    gameState = _gameState
    change = []
    playerSymbols = _playerSymbols
    currentPlayer = _currentPlayer
    playedCells = _playedCells
    printGameState(gameState)
    print(f"Player {currentPlayer}, make your move")
    change.append(int(input("What X position do you want to play? : ")) - 1)
    change.append(int(input("What Y position do you want to play? : ")) - 1)
    print(change)
    # check bool array for whether cell has been taken
    if not playedCells[change[0]][change[1]]:
        gameState[change[0]][change[1]] = playerSymbols[currentPlayer]
        playedCells[change[0]][change[1]] = True
    else:
        print("Cell has already been played")
    printGameState(gameState)


def game(_beginningGameState, _playerSymbols, _currentPlayer, _playedCells):
    playerSymbols = _playerSymbols
    playedCells = _playedCells
    currentGameState = _beginningGameState
    currentPlayer = _currentPlayer
    return newRound(currentGameState, playerSymbols, currentPlayer, playedCells)


def setup():
    # basic setup
    emptySymbol = input("what symbol should an empty cell have?\n")
    playerSymbols = []
    playerSymbols.append(input("what symbol should player 1 have?\n"))
    playerSymbols.append(input("what symbol should player 2 have?\n"))
    print(playerSymbols)
    # player 1 is displayed as player 0, player 2 is displayed as player 1
    # this is done to make array indexes easier
    currentPlayer = 0
    # plan: have gamestate be stored in 2d array
    # played cells will be stored in separate array, this makes stuff easier
    playedCells = [
        [False, False, False],
        [False, False, False],
        [False, False, False],
    ]
    beginningGameState = [
        [emptySymbol, emptySymbol, emptySymbol],
        [emptySymbol, emptySymbol, emptySymbol],
        [emptySymbol, emptySymbol, emptySymbol],
    ]
    game(beginningGameState, playerSymbols, currentPlayer, playedCells)


def main():
    setup()


main()
