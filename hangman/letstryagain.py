import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

        
def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    guessed = list("")
    for i in range(len(alphabet)):
        guess = input("Type in a letter: ")
        guess = guess.lower()
        if alphabet[i] == guess:
            guessed.append(str(guess))
            return guessed
            
def getAvailableLetters(lettersGuessed):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    listed = list(alphabet)
    for i in range(len(alphabet)):
        guess = input("Type in a letter: ")
        guess = guess.lower()
        if alphabet[i] == guess:
            listed.remove(str(guess))
            print(' '.join(listed))
            
def hangman(secretWord):
    length = len(secretWord)
    print("Welcome to hangman! The word you are guessing " +
          "contains " + str(length) + " letters. \n" +
          "Please only type in ONE letter per round. You ready?")
    while isWordGuessed(secretWord, lettersGuessed) is False:
        print(getAvailableLetters(lettersGuessed))
        print(getGuessedWord(secretWord, lettersGuessed))

secretWord = chooseWord("words.txt")
lettersGuessed = list("")
print(hangman(secretWord))












