

def getAvailableLetters(lettersGuessed):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    listed = list(alphabet)
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
lettersGuessed = list("")
print(getAvailableLetters(lettersGuessed))
