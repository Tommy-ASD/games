import random
from words.wordleWords import fiveLetterWords
from termcolor import colored
import time

allWords = fiveLetterWords
correctWord = None
playerWords = []
inputColors = []


def pickWord():
    global correctWord
    i = random.randint(0, len(allWords))
    correctWord = allWords[i]
    print(correctWord)


def showGuesses():
    # OPTIMIZE THIS
    for i in range(100):
        print("\n")
    for i in range(len(inputColors)):
        print(
            inputColors[i][0]
            + inputColors[i][1]
            + inputColors[i][2]
            + inputColors[i][3]
            + inputColors[i][4]
        )


def game(_curPlayerInput):
    global correctWord
    tempCorrectWord = correctWord
    curPlayerInput = _curPlayerInput
    # append every guessed word to a nested array
    inputColors.append([])
    for i in range(len(curPlayerInput)):
        # OPTIMIZE THIS
        if curPlayerInput[i] == tempCorrectWord[i]:
            # added len(inputColors) - 1 due to avoid errors
            inputColors[len(inputColors) - 1].append(
                colored(f"{str(curPlayerInput[i])}", "green")
            )
        elif curPlayerInput[i] in tempCorrectWord:
            inputColors[len(inputColors) - 1].append(
                colored(f"{str(curPlayerInput[i])}", "yellow")
            )
        else:
            inputColors[len(inputColors) - 1].append(
                colored(f"{str(curPlayerInput[i])}", "red")
            )

    showGuesses()

    if curPlayerInput == correctWord:
        print(f"guessed correct in {len(inputColors)}")
        if len(inputColors) > 6:
            print("This would count as a loss in normal Wordle")
        return True


def playerInput():
    # OPTIMIZE THIS
    while True:
        curPlayerInput = input()
        playerWords.append(curPlayerInput)
        if curPlayerInput == "giveUp":
            print(correctWord)
        # make sure word meets requirements
        if len(curPlayerInput) == 5:
            if curPlayerInput in allWords:
                # if word is correct, game returns True
                if game(curPlayerInput):
                    return False
            else:
                print("Not in word list")
                # find another way to do this
                time.sleep(3)
                showGuesses()
        else:
            print("Word is not 5 characters")
            time.sleep(3)
            showGuesses()


def main():
    pickWord()
    playerInput()


main()
