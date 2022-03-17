import random
from words.wordleWords import fiveLetterWords


def pickWord():
    global correctWord
    i = random.randint(0, len(fiveLetterWords))
    correctWord = fiveLetterWords[i]
    print(correctWord)


def checkWord():
    connectedWord = []
    global correctWord
    for i in range(len(correctWord)):
        connectedWord.append(correctWord[i])
        print(correctWord[i])
    print(
        connectedWord[0]
        + connectedWord[1]
        + connectedWord[2]
        + connectedWord[3]
        + connectedWord[4]
    )


def main():
    pickWord()
    checkWord()


main()
