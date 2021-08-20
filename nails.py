nailsNeeded = []
nailsOwned = []

def applyNails():
    global nailsNeeded
    global nailsOwned

    nailsNeeded.sort(reverse=True)
    nailsOwned.sort(reverse=False)

    print(nailsNeeded, nailsOwned)

    nailsToBuy = []

    for nailNeeded in nailsNeeded:
        foundNail = False
        for i, nailOwned in enumerate(nailsOwned):
            if(nailOwned >= nailNeeded): 
                foundNail = True
                nailsOwned.pop(i)
                print("found nail:", nailOwned, nailNeeded)
                break
        if(not foundNail):
            nailsToBuy.append(nailNeeded)

    nailsToBuy.sort()

    return nailsToBuy
        

def gatherInfo():
    amountNeeded = int(input("Hur många spikar behöver du?"))
    amountOwned = int(input("Hur många spikar har du?"))

    for i in range(amountNeeded):
        nailsNeeded.append(int(input("Behöver längd?")))

    for i in range(amountOwned):
        nailsOwned.append(int(input("Har längd?")))


def main():
    gatherInfo()
    nailsToBuy = applyNails()

    print("Antal:", len(nailsToBuy))
    print("Längder:", nailsToBuy)
    
    




main()