from wordleWords import fiveLetterWords


def checkWords():
    for i in range(len(fiveLetterWords)):
        if (
            "s" in fiveLetterWords[i][0]
            and "e" in fiveLetterWords[i][2]
            and "l" in fiveLetterWords[i][4]
        ):
            print(fiveLetterWords[i])


def inputWord():
    inputedWord = input("Input word here\n")
    inputedOutputs = input("Input results here\n")
    pass


def main():

    checkWords()


main()
