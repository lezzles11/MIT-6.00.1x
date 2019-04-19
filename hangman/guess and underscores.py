"""

not sure how to identify and replace the letter in the word 
e.g., if user typed in letter 'a'
it would print back out 
a _____


>>> s = list("Hello zorld")
>>> s
['H', 'e', 'l', 'l', 'o', ' ', 'z', 'o', 'r', 'l', 'd']
>>> s[6] = 'W'
>>> s
['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
>>> "".join(s)
'Hello World'

turn it into a list first


word = 'apple'
wordAsList = list(word)
print(wordAsList)
underscores = len(word) * str('_')

for n, i in enumerate(wordAsList):
    guess = input("guess a letter: ")
    i = guess
    if i == [n]:
        underscores[n] = i
        print(underscores)
"""
word = ['a', 'p', 'p', 'l', 'e']
guess = 'a'
underscores = len(word) * str('_')
underscores1 = map(lambda x: list.replace(x, "_", guess), underscores)
print(underscores1)



