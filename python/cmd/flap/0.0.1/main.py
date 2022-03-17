import random

gameState = []


def display():
    for i in range(len(gameState)):
        print(gameState[i])

#def bird():


def pipes():
    yPos = random(len(gameState[0]))
    for i in range(len(gameState)):
        

def main():
    # playerInputxLength = int(input("How long do you want the console display to be?"))
    # playerInputyLength = int(input("How long do you want the console display to be?"))
    xLength = 10
    yLength = 19
    for i in range(xLength):
        gameState.append([])
        for j in range(yLength):
            gameState[i].append([])
            gameState[i][j].append(".")
    display()


main()
