
def formulaIndexArrayToString(formulaIndexArray, letters):
    res = ""
    for formulaPart in formulaIndexArray:
        if formulaPart == -1:
            continue

        res += letters[formulaPart]

    return res