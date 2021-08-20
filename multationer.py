end = ""
biome = []
letters = ["A", "B", "C"]

def clearItemsBelow(index, array):
    print("-------", array, index)
    for i in range(index):
        array[i] = 0

    print("=========", array)
    return array


def formulaIndexArrayToString(formulaIndexArray):
    res = ""
    for formulaPart in formulaIndexArray:
        if formulaPart == -1:
            continue

        res += letters[formulaPart]

    return res


def mutate(innerBiome, specieI, formulaIndexArray):
    formulaStr = formulaIndexArrayToString(formulaIndexArray)
    print("hi", formulaStr)


def createMutants(innerBiome, specieI, currentMutationFormulaIndexArray):
    while True:
        for i, mutationFormulaPartIndex in enumerate(currentMutationFormulaIndexArray):
            if mutationFormulaPartIndex < len(letters) - 1:
                currentMutationFormulaIndexArray[i] += 1
                mutate(innerBiome, specieI, currentMutationFormulaIndexArray)
                currentMutationFormulaIndexArray = clearItemsBelow(i, currentMutationFormulaIndexArray)
                break

    

def evolve(innerBiome):
    for i, specieOrSpecies in enumerate(innerBiome):
        if isinstance(specieOrSpecies, list):
            evolve(specieOrSpecies)
        else:
            innerBiome[i] = createMutants(innerBiome, i, [-1] * len(letters))

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