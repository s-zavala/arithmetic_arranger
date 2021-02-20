"""
Accepts a list of problem strings.
        an optional True or False arg.
Returns a vertically formated problem with an optional answer.

Sofia Zavala
02.15.2021
"""
from separate import separate
from answer import answer
from format_lines import format_lines

def arithmetic_arranger(problems, solution = False):
    """
    Takes a list of addition or subtraction problems and reformats the problems vertically for easy reading.
    """
    fieldKey=['probStr','term1','term2', 'operator', 'len1', 'len2', 'colWidth', 'sum']
    mainDict = {}

    # Test problems argument for five or fewer elements.
    pcopy = problems[:]
    if (len(pcopy) > 5):
        return "Error: Too many problems."

    # Apply separate() to each problem to break down into parts.
    # Log parts into the main Dictionary under numerical keys.
    counter = 0
    for prob in problems:
        aDict = separate(prob)
        if type(aDict) == str:
            return aDict
        mainDict['Problem%s' % str(counter + 1)] = aDict
        counter += 1

    # Add solutions to problems if optional arg is True.
    if solution == True:
        mainDict = answer(mainDict)

    # Apply format_lines() to each problem key in mainDict.
    arranged_problems = format_lines(mainDict, solution)
    return arranged_problems

if __name__ == '__main__':
    testSuite = (["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],
                ["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "1 + 99"],
                ["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "1 + 100", "1 + 100"],
                ["32 * 698", "3801 + 2", "45 + 43", "123 + 123"],
                ["32 + 698", "38a1 + 2", "45 + 43", "123 + 123"],
                ["32 + 698", "3801 + 2", "45678 + 43", "123 + 123"])
    for test in testSuite:
        print(arithmetic_arranger(test))
    print(arithmetic_arranger(problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], solution = True))
