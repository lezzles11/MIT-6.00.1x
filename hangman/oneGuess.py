secretWord = 'apple'

#split it up into individual letters 
copyAnswer = list(secretWord)

#guessedLetters in a list
guessedLetters = list()
print(copyAnswer)

#in the range of the letters of Secret Word
for i in range (len(secretWord)):
    #replace every letter with '_' 
    copyAnswer[i] = '_'
    #but when you print it, make sure you join the whole thing
    print(' '.join(copyAnswer))
    
    
count = 0
#
for i in range (len(secretWord)):
    guess = input("Type in a letter: ")
    guess = guess.lower()
    count = count + 1 
    if secretWord[i] == guess:
        copyAnswer[i] = guess
        print(' '.join(copyAnswer))
        print()
        print("nice job!")
    else:
        print("No")
        guessedLetters.append(guess)
        print(guessedLetters)

