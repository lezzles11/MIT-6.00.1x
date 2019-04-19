#LEZZGO

import random

WORDLIST_FILENAME = "words.txt"
def main():
    secretWord = ""
    wordlist = loadWords()
    length = len(secretWord)
    copyAnswer = list(secretWord)
    count = 0
    copy = str(secretWord)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    listed = list(alphabet)
    guessed = list("")
    listedNotGuessed = "You have not guessed " + str(listed) + " letters yet."
    guess = input("Type in a letter: ")
    guess = guess.lower()
    isWordGuessed() 


def hangman(secretWord):
    print("Welcome to hangman! The word you are guessing " +
          "contains " + str(length) + " letters. \n" +
          "Please only type in ONE letter per round. You ready?")
    isWordGuessed(secretWord, lettersGuessed)
    getGuessedWord(secretWord, lettersGuessed)

print(hangman(secretWord))

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


