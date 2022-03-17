# needs fixing:
# all letters in a guessed word light up yellow even if it's only 1 of the correct letters in the correct word

import random
from words.wordleWords import fiveLetterWords
from termcolor import colored
import time
from os import system

allWords = fiveLetterWords
correctWord = None
playerWords = []
inputColors = []


def pickWord():
    global correctWord
    i = random.randint(0, len(allWords))
    correctWord = allWords[i]


def showGuesses():
    # # # OPTIMIZE THIS
    # # # print empty line a hundred times to skip past guess
    # # # for i in range(100):
    # # #     print("\n")
    # # less effective?
    # # imports entire module
    # # os.system("cls")
    # instead of import os, write from os import system
    system("cls")
    for i in range(len(inputColors)):
        # OPTIMIZE THIS
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
                print("Not in word list (press enter to continue)")
                # find another way to do this
                input()
                showGuesses()
        else:
            print("Word is not 5 characters (press enter to continue)")
            input()
            showGuesses()


def main():
    pickWord()
    playerInput()


main()
