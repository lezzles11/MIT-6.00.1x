# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

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

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
length = len(secretWord)
copyAnswer = list(secretWord)
count = 0
copy = str(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
listed = list(alphabet)
guessed = list("")
listedNotGuessed = "You have not guessed " + str(listed) + " letters yet."
        

def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        guess = input("Type in a letter: ")
        if guess == secretWord:
            print("Wow - Nice job!")
        else:
            print("try again")

def getGuessedWord(secretWord, lettersGuessed):
    for i in range(len(alphabet)):
        guess = input("Type in a letter: ")
        guess = guess.lower()
        if alphabet[i] == guess:
            guessed.append(str(guess))
            print(guessed)
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    

def getAvailableLetters(lettersGuessed):
    for i in range(len(alphabet)):
        guess = input("Type in a letter: ")
        guess = guess.lower()
        if alphabet[i] == guess:
            listed.remove(str(guess))
            print(' '.join(listed))
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    

def hangman(secretWord):
    print("Welcome to hangman! The word you are guessing " +
          "contains " + str(length) + " letters. \n" +
          "Please only type in ONE letter per round. You ready?")
    
    getGuessedWord(secretWord, lettersGuessed)
    isWordGuessed(secretWord, lettersGuessed)
'''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.DONE
'''

'''
Ask the user to supply one guess per round. DONE
'''

'''
The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
'''
'''
After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

Follows the other limitations detailed in the problem write-up.
'''
    # FILL IN YOUR CODE HERE...






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
