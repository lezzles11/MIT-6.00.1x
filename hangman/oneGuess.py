"""

#split it up into individual letters 


#guessedLetters in a list

print(copyAnswer)

#in the range of the letters of Secret Word
for i in range (len(secretWord)):
    #replace every letter with '_' 
    copyAnswer[i] = '_'
    #but when you print it, make sure you join the whole thing
    print(' '.join(copyAnswer))
    
"""
count = 0
secretWord = 'apple'
copyAnswer = list(secretWord)
guessedLetters = list()
#
for i in range (len(secretWord)):
    guess = input("Type in a letter: ")
    guess = guess.lower()
    i = 0
    if secretWord[i] == guess:
        copyAnswer[i] = guess
        print(' '.join(copyAnswer))
        print()
        print("nice job!")
    else:
        print("No")
        guessedLetters.append(guess)
        print(guessedLetters)


