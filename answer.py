def answer(mainDict):
    """
    Args: mainDict
    Returns: mainDict with added key/value pairs for each problem.
        key: 'sum'
        value: problem solution as an int
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