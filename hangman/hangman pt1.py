"""
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
takes a tuple as input, and returns new tuple as output
every other element of the tuple is printed

"""

def oddTuples(aTup):
    tup = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            tup = tup + (aTup[i],)
    return tup

aTup = ('I', 'am', 'a', 'test', 'tuple')
lup = oddTuples(aTup)
print(lup)


"""
"""

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


def addOne(b):
    return b + 1


def square(c):
    return c**2



testList = [1, -4, 8, -9]

copy1 = testList[:]
applyToEach(copy1, abs)
print(copy1)


copy2 = testList[:]
applyToEach(copy2, addOne)
print(copy2)

copy3 = testList[:]
applyToEach(copy3, square)
print(copy3)
