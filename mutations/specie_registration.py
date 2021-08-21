import math
import mutation_path
import sys

registeredSpecies = []

def isBigger(DNA, i):
    opponent = registeredSpecies[i]

    if len(opponent) != len(DNA): return len(opponent) < len(DNA)
    for i, letter in enumerate(DNA):
        opponentsLetter = opponent[i]
        if(letter == opponentsLetter):
            continue
        else: return letter > opponentsLetter

    return False #Is Equal


def standardSearch(DNA):
    #print("std search")
    for i in range(len(registeredSpecies)):
        if not isBigger(DNA, i):
            return i


#def binarySearch(DNA, i, biggest = 0, smallest):


def findRightPosition(DNA, i):
    if len(registeredSpecies) == 0 or isBigger(DNA, len(registeredSpecies)-1): return -1
    if not isBigger(DNA, 0): return 0
    if len(registeredSpecies) < 3 or True: return standardSearch(DNA)



    '''
    if(i > len(registeredSpecies)-1):
        return-1
    if(i < 0):
        return -2
    if(biggest -2 == smallest):
        return i

    isBiggerAns = isBigger(DNA, i)
    newI = 0

    print("isBigger:", isBiggerAns)

    if(isBiggerAns == None):
        return i
    elif(isBiggerAns):
        biggestRefPoint = biggest if biggest > i else len(registeredSpecies) - 1
        newI = math.ceil((biggestRefPoint - i) / 2 + i)
    else:
        smallestRefPoint = smallest if smallest < i else 0
        newI = math.floor((i - smallestRefPoint) / 2 + smallestRefPoint)

    if(newI == i):
        newI = newI+1 if isBiggerAns else newI -1
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
    return
    sys.setrecursionlimit(150)

    while True:
        specie = mutation_path.MutationPath(DNA=input("DNA: "), path=[])
        hasSpecieOrRegister(specie)

        print(registeredSpecies)

test()