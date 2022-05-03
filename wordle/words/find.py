from wordleWords import fiveLetterWords


def main():
    for i in range(len(fiveLetterWords)):
        if (
            "w" not in fiveLetterWords[i][0]
            and "w" in fiveLetterWords[i]
            and "o" in fiveLetterWords[i]
            and "h" in fiveLetterWords[i][1]
        ):
            print(fiveLetterWords[i])


main()
