from wordleWords import fiveLetterWords


def main():
    for i in range(len(fiveLetterWords)):
        if (
            "u" in fiveLetterWords[i]
            and "g" in fiveLetterWords[i]
            and "e" in fiveLetterWords[i][4]
            and "g" not in fiveLetterWords[i][4]
            and "u" not in fiveLetterWords[i][2]
            and "g" not in fiveLetterWords[i][2]
            and "u" not in fiveLetterWords[i][3]
            and "l" not in fiveLetterWords[i]
            and "f" not in fiveLetterWords[i]
            and "v" not in fiveLetterWords[i]
            and "a" not in fiveLetterWords[i]
        ):
            print(fiveLetterWords[i])


main()
