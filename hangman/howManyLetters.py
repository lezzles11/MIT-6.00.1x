
def howManyLetters(secretWord):
    length = len(secretWord)
    print("Welcome to hangman! The word you are guessing "
      "contains " + str(length) + " letters. You ready?")
    

    
def hangman(secretWord):
    print("Welcome to hangman! The word you are guessing " +
          "contains " + str(length) + " letters. \n" +
          "Please only type in ONE letter per round. You ready?")
    howManyLetters(secretWord)

secretWord = 'apple'
length = len(secretWord)

print(hangman(secretWord))
