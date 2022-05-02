from wordleWords import fiveLetterWords


def main():
    for i in range(len(fiveLetterWords)):
        if (
            "s" in fiveLetterWords[i][2]
            and "t" in fiveLetterWords[i][3]
            and "y" in fiveLetterWords[i][4]
            and "w" not in fiveLetterWords[i]
            and "o" not in fiveLetterWords[i]
            and "a" not in fiveLetterWords[i]
            and "m" not in fiveLetterWords[i]
            and "b" not in fiveLetterWords[i]
            and "u" not in fiveLetterWords[i]
            and "n" not in fiveLetterWords[i]
            and "i" not in fiveLetterWords[i]
        ):
            print(fiveLetterWords[i])


main()
