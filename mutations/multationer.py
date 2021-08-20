import time
from mutation_path import MutationPath

start = ""
end = ""
biome = ""
letters = ["A", "B", "C"]
deathTol = 0
amountIndividuals = 0
successfullSpecies = []
    

def isMutationBeneficial(parent, newSpecie):
    global deathTol
    global successfullSpecies

    if newSpecie.DNA == end:
        print("==============", start, "+", newSpecie.path, "=>", newSpecie.DNA)
        successfullSpecies += newSpecie
    elif len(newSpecie.DNA) > len(end): pass
    elif newSpecie.DNA == parent.DNA: pass
    else: return True

    deathTol += 1

    if(deathTol % 100 == 0):
        print("Population Size", amountIndividuals,  "Deathtol", deathTol, "Latest Death:", newSpecie)
    return False


def formulaIndexArrayToString(formulaIndexArray):
    res = ""
    for formulaPart in formulaIndexArray:
        if formulaPart == -1:
            continue

        res += letters[formulaPart]

    return res


def mutate(innerBiome, specieI, formulaIndexArray, originalSpicie):
    global amountIndividuals

    formulaStr = formulaIndexArrayToString(formulaIndexArray)

    for letter in letters:
        newSpecie = MutationPath(originalSpicie.DNA.replace(letter, formulaStr), path=originalSpicie.path + [formulaStr])

        if isMutationBeneficial(originalSpicie, newSpecie):
            innerBiome[specieI].append(newSpecie)
            amountIndividuals += 1
            registrerSpecie(newSpecie)


def createMutants(innerBiome, specieI):
    global amountIndividuals

    originalSpecie = innerBiome[specieI]
    innerBiome[specieI] = []
    amountIndividuals -= 1
    intFormula = [-1] * len(letters)
    directionArr = [1] * len(letters)
    run = True

    while run:
        for i in range(len(intFormula)):
            time.sleep(0.1)
            intFormula[i] += directionArr[i]

            if intFormula[i] == -1 or intFormula[i] == len(letters):
                if i == len(intFormula) -1:
                    return

                directionArr[i] *= -1
                intFormula[i] += directionArr[i]
                continue

            mutate(innerBiome, specieI, intFormula, originalSpecie)

            break
            
def evolve(innerBiome):
    hasCreatedNew = False

    for i, specieOrSpecies in enumerate(innerBiome):
        if isinstance(specieOrSpecies, list):
            return evolve(specieOrSpecies)
        else:
            createMutants(innerBiome, i)
            hasCreatedNew = True

    return hasCreatedNew

def evolution():
    i = 1
    while evolve(biome):
        if len(successfullSpecies) > 0:
            break
        i += 1
        print("Generation:", i)
    print("EXPERMIENT CONCLUDED", successfullSpecies)


def getInput():
    global biome
    global end
    global start

    start = input("Start ?")
    biome = [MutationPath(DNA = start, path=[])]
    end = input("mål   ?")
    

def main():
    getInput()
    evolution()


main()
