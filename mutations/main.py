from mutation_path import MutationPath
import evolution


def getInput():
    global biome
    global end
    global start

    start = input("Start ?")
    biome = [MutationPath(DNA = start, path=[])]
    end = input("mål   ?")

    return {"start": start, "biome": biome, "end":end}

def main():
    inputObj = getInput()
    evolutionObj = evolution.Evolution(inputObj["start"], inputObj["biome"], inputObj["end"])
    evolutionObj.doEvolution()

main()
