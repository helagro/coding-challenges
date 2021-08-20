import time

end = ""
biome = []
letters = ["A", "B", "C"]

def formulaIndexArrayToString(formulaIndexArray):
    res = ""
    for formulaPart in formulaIndexArray:
        if formulaPart == -1:
            continue

        res += letters[formulaPart]

    return res


def mutate(innerBiome, specieI, formulaIndexArray, originalSpicie):
    formulaStr = formulaIndexArrayToString(formulaIndexArray)

    for letter in letters:
        newSpecie = originalSpicie.replace(letter, formulaStr)
        innerBiome[specieI].append(newSpecie)

        if(newSpecie == end):
            print(originalSpicie, "+", formulaStr, "=>", newSpecie)


def createMutants(innerBiome, specieI):
    originalSpecie = innerBiome[specieI]
    innerBiome[specieI] = []
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
    for i, specieOrSpecies in enumerate(innerBiome):
        if isinstance(specieOrSpecies, list):
            evolve(specieOrSpecies)
        else:
            createMutants(innerBiome, i)

def evolution():
    while True:
        evolve(biome)


def getInput():
    global biome
    global end

    biome = [input("Start ?")]
    end = input("mål   ?")
    

def main():
    getInput()
    evolution()



main()