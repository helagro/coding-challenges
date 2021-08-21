import math
import mutation_path
import sys

registeredSpecies = []

def guessIsBigger(DNA, i):
    opponent = registeredSpecies[i]

    if len(opponent) != len(DNA): return len(opponent) < len(DNA)
    for i, letter in enumerate(DNA):
        opponentsLetter = opponent[i]
        if(letter == opponentsLetter):
            continue
        else: return letter > opponentsLetter

    return False #Is Equal


def binarySearch(DNA):
    smallestAbove = len(registeredSpecies) -1
    biggestUnderneath = 0
    while True:
        guessI = round((smallestAbove - biggestUnderneath) / 2 + biggestUnderneath)
        guessIsBiggerAns = guessIsBigger(DNA,guessI)
        print("dwa", guessI)

        if guessIsBiggerAns: biggestUnderneath = guessI
        else: smallestAbove: smallestAbove = guessI
        if(smallestAbove - biggestUnderneath <= 1): return smallestAbove


def standardSearch(DNA):
    print("std search")
    for i in range(len(registeredSpecies)):
        if not guessIsBigger(DNA, i):
            return i


def findRightPosition(DNA, i):
    if len(registeredSpecies) == 0 or guessIsBigger(DNA, len(registeredSpecies)-1): return -1
    #if not guessIsBigger(DNA, 0): return 0
    #if len(registeredSpecies) < 3: return standardSearch(DNA)

    return binarySearch(DNA)

    '''
    if(i > len(registeredSpecies)-1):
        return-1
    if(i < 0):
        return -2
    if(biggest -2 == smallest):
        return i

    guessIsBiggerAns = guessIsBigger(DNA, i)
    newI = 0

    print("guessIsBigger:", guessIsBiggerAns)

    if(guessIsBiggerAns == None):
        return i
    elif(guessIsBiggerAns):
        biggestRefPoint = biggest if biggest > i else len(registeredSpecies) - 1
        newI = math.ceil((biggestRefPoint - i) / 2 + i)
    else:
        smallestRefPoint = smallest if smallest < i else 0
        newI = math.floor((i - smallestRefPoint) / 2 + smallestRefPoint)

    if(newI == i):
        newI = newI+1 if guessIsBiggerAns else newI -1
    if(biggest < i):
        biggest = i
    elif(smallest > i):
        smallest = i

    return findRightPosition(DNA, newI, biggest, smallest, i) '''


def hasSpecieOrRegister(specie):
    i = findRightPosition(specie.DNA, round(len(registeredSpecies) / 2))

    if(i != -1 and specie.DNA == registeredSpecies[i]):
        #print("Already has specie")
        return True

    if(i == -1): registeredSpecies.append(specie.DNA)
    else: registeredSpecies.insert(i, specie.DNA)

    return False



def test():
    
    sys.setrecursionlimit(150)

    while True:
        specie = mutation_path.MutationPath(DNA=input("DNA: "), path=[])
        hasSpecieOrRegister(specie)

        print(registeredSpecies)

test()