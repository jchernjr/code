#include <iostream>

using namespace std;

string pickWord()
{
    // TODO: Actually randomize later.
    return "WE'RE TRYING TO CODE HANGMAN";
}

/*
 * Converts a string of input words into a string of underscores,
 * where each letter in the input string becomes an underscore, and
 * spaces remain spaces.
 *
 * "THIS IS SOME SECRET"
 * "____ __ ____ ______"
 */
string makeUnderscores(string input)
{
    string output;
    for (unsigned int i = 0; i < input.length(); i++)
    {
        char c = input[i];
        if (c >= 'A' && c <= 'Z')
        {
            output += ".";
        }
        else
        {
            output += c;
        }
    }

    return output;
}

/*
 * Returns whether the secret string contains the guessed char.
 */
bool checkGuess(string secret, char guess)
{
    return secret.find(guess) != string::npos;
}

void playGame(string secret)
{
    string progress = makeUnderscores(secret);
    cout << progress << endl;

    char guess;
    cout << "Guess a letter: ";
    cin >> guess;
    string guessStr = "" + guess;

    if (checkGuess(secret, guess))
    {
        // replace corresponding spaces in 'progress' string
        for (unsigned int i = 0; i < secret.length(); i++)
        {
            if (guess == secret[i])
            {
                progress = progress.substr(0, i) + guess + progress.substr(i+1);
            }
        }
        cout << progress << endl;
    }
    else
    {
        cout << "You only get one wrong guess, so you lose." << endl;
    }
}

int main()
{
    string word = pickWord();
    playGame(word);
    return 0;
}
