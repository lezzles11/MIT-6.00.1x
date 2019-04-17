"""
getGuessedWord = takes in secret word (string) and lettersGuessed (list of letters)
return string based on what letters in lettersGuessed are in secretWord
should not be too different from isWordGuessed


first, type in 

#For whatever 
def convert(list1):
    for i in range(len(list1):
                   list1[i] = 

#

def isWordGuessed(secretWord, lettersGuessed):
    count = 0
    for i, c in enumerate(secretWord):
        if c in lettersGuessed:
            count = count + 1
    if count == len(secretWord):
        return True 
    else:
        return False
"""
def getGuessedWord(secretWord, lettersGuessed):
    count = 0
    #turn secretWord into a list
    listed = list(secretWord)
    #looping around every object in secretWord
    for i, c in enumerate(listed):
        #if guess not in secretWord
        if c not in listed:
            #replace that with the underscore 
            a[i] -= a['_']
        else:
            pass
    print(listed)

getGuessedWord("apple", "a")



            

