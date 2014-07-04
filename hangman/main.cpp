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

void playGame(string secret)
{
    string progress = makeUnderscores(secret);
    cout << progress << endl;
}

int main()
{
    string word = pickWord();
    playGame(word);
    return 0;
}
