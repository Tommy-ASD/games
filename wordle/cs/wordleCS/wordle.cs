using System;
using vars;
class wordle
{
    public string word;
    public bool running;
    static void Main(string[] args)
    {
        while (true)
        {
            wordle game = new wordle();
            while (game.running)
            {
                Console.WriteLine("Guess a word");
                game.playerInput(Console.ReadLine());
            }
        }
    }

    public wordle()
    {
        wordlist wrds = new wordlist();
        string[] words = wrds.getWords();
        start(words);
        running = true;
    }
    string[] words;
    char[][] inputtedColors;

    public void start(string[] words)
    {
        this.pickWord(words);
        this.words = words;
    }

    public void pickWord(string[] words)
    {
        Random rand = new Random();
        int randomNumber = rand.Next(0, words.Length);
        this.word = words[randomNumber];
    }

    public void playerInput(string guessedWord)
    {
        if (!this.running)
        {
            return;
        }
        if (guessedWord == null)
        {
            Console.WriteLine("Please provide a guess");
            return;
        }
        if (guessedWord == "giveUp")
        {
            Console.WriteLine("fucking pussy lmao");
            Console.WriteLine(this.word);
            this.running = false;
            return;
        }
        if (guessedWord.Length != 5)
        {
            Console.WriteLine("Word is not five characters");
            return;
        }
        foreach (string wrd in words)
        {
            Console.WriteLine(wrd);
        }
        int pos = Array.IndexOf(words, word);
        if (pos <= -1)
        {
            Console.WriteLine("Word is not in word list");
            return;
        }
        if (this.game(guessedWord.ToLower()))
        {
            this.running = false;
            Console.WriteLine("Guessed correct in {this.inputtedColors.Length}");
            return;
        }
    }

    public bool game(string guessedWord)
    {
        char[] charGuess = new char[guessedWord.Length];
        char[] charWord = new char[this.word.Length];
        for (int i = 0; i < charGuess.Length; i++)
        {
            charGuess[i] = guessedWord[i];
            charWord[i] = this.word[i];
        }
        Console.WriteLine(green(charGuess, charWord));
        //this.inputtedColors.Append();
        if (guessedWord == this.word)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    public char[] green(char[] guess, char[] word)
    {
        char[] lInputColors = { 'b', 'b', 'b', 'b', 'b' };
        for (int i = 0; i < guess.Length; i++)
        {
            if (guess[i] == word[i])
            {
                guess[i] = '*';
                word[i] = '¨';
                lInputColors[i] = 'g';
            }
        }
        return (yellow(guess, word, lInputColors));
    }
    public char[] yellow(char[] guess, char[] word, char[] lInputColors)
    {
        for (int i = 0; i < guess.Length; i++)
        {
            if (word.Contains(guess[i]))
            {
                int ind = Array.IndexOf(word, guess[i]);
                Console.WriteLine(ind);
                Console.WriteLine(guess[i]);
                Console.WriteLine(word);
                word[ind] = '¨';
                guess[i] = '*';
                lInputColors[i] = 'y';
            }
        }
        foreach (char str in lInputColors)
        {
            Console.WriteLine(str);
        }
        Console.WriteLine(lInputColors);
        return (lInputColors);
    }

}

