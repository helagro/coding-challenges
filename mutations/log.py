import time

def mainStats(prefix, successfullSpecies, populationsize, deathtol):
    print(prefix, "SuccessfullSpecies", successfullSpecies, "Population Size", populationsize,  "Deathtol", deathtol)


doDebug = False
def debug(*args):
    if not doDebug: return
    print("Debug", args)
    time.sleep(0.2)