def answer(mainDict):
    """
    Updates the main dict key 'sum' for each problem with value of the answer as a str.

    Args:
    mainDict -- a main dict
    Returns:
    mainDict -- updated main dict with key 'sum' and value of the solution as a str.
    """
    for prob in mainDict.keys():
        term1 = int(mainDict[prob]['term1'])
        term2 = int(mainDict[prob]['term2'])
        operator = mainDict[prob]['operator']
        sum = 0
        if operator == '+':
            sum = term1 + term2
        else:
            sum = term1 - term2
        mainDict[prob]['sum'] = str(sum)
    return mainDict