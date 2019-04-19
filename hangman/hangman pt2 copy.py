"""
This is if letter is guessed:

def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        guess = input("Put in a letter: ")
        if guess in secretWord:
            lettersGuessed.append(guess)
            return True
            guess = ""
        else:
            return False
            continue
            lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
            lettersGuessed = ['a', 'p', 'p', 'l', 'e']
            
"""
            
def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if i not in lettersGuessed:
            print("a!")
        elif i in lettersGuessed:
            print('b!')
            continue
    if lettersGuessed in list(secretWord):
        return True
    else:
        return False
lettersGuessed = ['a', 'p', 'p', 'l', 'e']
secretWord = 'apple'

print(isWordGuessed(secretWord, lettersGuessed))
