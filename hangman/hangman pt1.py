def isWordGuessed(secretWord, lettersGuessed):
    count = 0
    copy = str(secretWord)
    for i in secretWord:
        guess = input("Guess the word: ")
        if guess == secretWord:
            print("Wow - Nice job!")
        else:
            print("try again")

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))
