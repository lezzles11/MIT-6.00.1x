"""
def apply(L, F):
    assuming L is a list, f is a function.
    replacing each element of L by f(e)
    for i in range(len(L)):
        L(i) = f(L[i])

Implement the function isWordGuess that takes two parameters:
1. String (secret word)
2. List of Letters (letters Guessed)

Function returns a Boolean - True value if SecretWord has been guessed
Otherwise, false will be printed 
#secretWord is a list
        
"""

def isWordGuessed(secretWord, lettersGuessed):
    count = 0
    for i, c in enumerate(secretWord):
        if c in lettersGuessed:
            count = count + 1
    if count == len(secretWord):
        return True 
    else:
        return False






