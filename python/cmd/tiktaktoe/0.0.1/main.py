from copyreg import constructor


gameState = []


def printGameState(_gameState):
    gameState = _gameState
    print(gameState[0])
    print(gameState[1])
    print(gameState[2])


def newRound(_gameState, _playerSymbols, _currentPlayer):
    gameState = _gameState
    change = []
    playerSymbols = _playerSymbols
    currentPlayer = _currentPlayer
    printGameState(gameState)
    print(f"Player {currentPlayer}, make your move")
    change.append(int(input("What X position do you want to play? : ")) - 1)
    change.append(int(input("What Y position do you want to play? : ")) - 1)
    print(change)
    gameState[change[0]][change[1]] = playerSymbols[currentPlayer]
    printGameState(gameState)
    return False


def game(_beginningGameState, _playerSymbols, _currentPlayer):
    playerSymbols = _playerSymbols
    currentGameState = _beginningGameState
    currentPlayer = _currentPlayer
    return newRound(currentGameState, playerSymbols, currentPlayer)


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
    beginningGameState = [
        [emptySymbol, emptySymbol, emptySymbol],
        [emptySymbol, emptySymbol, emptySymbol],
        [emptySymbol, emptySymbol, emptySymbol],
    ]
    game(beginningGameState, playerSymbols, currentPlayer)


def main():
    setup()


main()
