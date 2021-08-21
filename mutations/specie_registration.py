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
        #print("dwa", guessI)

        if guessIsBiggerAns: biggestUnderneath = guessI
        else: smallestAbove: smallestAbove = guessI
        if(smallestAbove - biggestUnderneath <= 1): return smallestAbove


def findRightPosition(DNA, i):
    if len(registeredSpecies) == 0 or guessIsBigger(DNA, len(registeredSpecies)-1): return -1
    return binarySearch(DNA)


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

#test()