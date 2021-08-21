import translators
from mutation_path import MutationPath
import fittness_test
import specie_registration
import log
import threading

class Evolution:
    def __init__(self, startDNA, biome, endDNA) -> None:
        self.startDNA = startDNA
        self.biome = biome
        self.endDNA = endDNA

    letters = "abc"
    deathTol = 0
    populationsize = 0
    successfullSpecies = []


    def childAcounting(self, specie, parentsHabitat, habitatI):
        if specie.DNA == self.endDNA:
            print("==============", self.startDNA, "+", specie.path, "=>", specie.DNA)
            self.successfullSpecies.append(specie)

        parentsHabitat[habitatI].append(specie)
        self.populationsize += 1

    def mutate(self, letter, formulaStr, parent):
        newDna = parent.DNA.replace(letter, formulaStr)
        newPath = parent.path + [(letter + " => " +formulaStr)]
        child = MutationPath(newDna, path=newPath)
        return child


    def mutateWithEveryLetterAndInc(self, parentsHabitat, habitatI, formulaStr, parent):
        global amountIndividuals
        global deathTol

        for letter in self.letters:
            child = self.mutate(letter, formulaStr, parent)
            if fittness_test.isMutationBeneficial(parent, child, self.endDNA):
                self.childAcounting(child, parentsHabitat, habitatI)
            else:
                self.deathTol += 1
                if(self.deathTol % 10000000 == 0):
                    log.mainStats("at mutate:", self.successfullSpecies, self.populationsize, self.deathTol)

    def killParent(self, parentsHabitat, habitatI):
        parentSpecie = parentsHabitat[habitatI]
        parentsHabitat[habitatI] = []
        self.populationsize -= 1
        return parentSpecie


    def mutateWithEveryFormula(self, parentsHabitat, habitatI):
        global amountIndividuals
        parentSpecie = self.killParent(parentsHabitat, habitatI)
        intFormula = [-1] * len(self.letters)
        directionArr = [1] * len(self.letters)

        while True:
            for i in range(len(intFormula)):
                intFormula[i] += directionArr[i]

                if intFormula[i] == -1 or intFormula[i] == len(self.letters):
                    if i == len(intFormula) -1:
                        return

                    directionArr[i] *= -1
                    intFormula[i] += directionArr[i]
                    continue

                formulaStr = translators.formulaIndexArrayToString(intFormula, self.letters)
                self.mutateWithEveryLetterAndInc(parentsHabitat, habitatI, formulaStr, parentSpecie)
                break
                
    def evolve(self, parentsHabitat):
        for i, childOrHabitat in enumerate(parentsHabitat):
            if isinstance(childOrHabitat, list):
                self.evolve(childOrHabitat)
            else:
                self.mutateWithEveryFormula(parentsHabitat, i)

    def doEvolution(self):
        i = 1

        while True:
            self.evolve(self.biome)

            if self.populationsize < 1:
                break
            if len(self.successfullSpecies) > 0:
                break

            i += 1
            log.mainStats("Generation: "+ str(i), self.successfullSpecies, self.populationsize, self.deathTol)

        log.mainStats("\nEXPERMIENT CONCLUDED\n", self.successfullSpecies, self.populationsize, self.deathTol)