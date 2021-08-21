import specie_registration
import log

def isMutationBeneficial(parent, child, endDNA):
    global deathTol
    global successfullSpecies
    isBeneficial = False

    if len(child.DNA) > len(endDNA): log.debug("fittnesTest:", "Too long")
    elif child.DNA == parent.DNA: log.debug("fittnesTest:", "Same as parent")
    elif specie_registration.hasSpecieOrRegister(child): log.debug("fittnesTest:", "already in db")
    else: isBeneficial =  True
    log.debug("fittness test: isBeneficial:", isBeneficial, "specie:", child, "parent:",parent)

    return isBeneficial