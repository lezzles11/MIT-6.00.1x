def getGuessedWord(secretWord, lettersGuessed):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    guessed = list("")
    for i in range(len(alphabet)):
        guess = input("Type in a letter: ")
        guess = guess.lower()
        if alphabet[i] == guess:
            guessed.append(str(guess))
            return guessed

secretWord = 'apple'
lettersGuessed = list("")
print(getGuessedWord(secretWord, lettersGuessed))
