def separate(prob):
    """
    Separate each problem into its components.

    Args:
    prob -- a problem string
    Returns:
    probDict -- a dict of keys that describe the problem components,
    and values which are ints for each component.
    """
    
    fieldKey=['probStr','term1','term2', 'operator', 'len1', 'len2', 'colWidth']
    terms=[prob]
    if ' + ' in prob:
        terms+=prob.split(' + ')
        terms.append('+')
        # print('Terms list: ', terms)
    elif ' - ' in prob:
        terms+=prob.split(' - ')
        terms.append('-')
        # print('Terms list: ', terms)
    else:
        return "Error: Operator must be '+' or '-'."
    charSet='1234567890'
    for char in terms[1]+terms[2]:
        if (char in charSet) == False:
            return 'Error: Numbers must only contain digits.'
    len1=len(terms[1])
    len2=len(terms[2])
    if len1 > 4 or len2 > 4:
        return 'Error: Numbers cannot be more than four digits.'
    terms.append(len1)
    terms.append(len2)
    colWidth=max(terms[-1], terms[-2])+2
    terms.append(colWidth)
    # print('Terms list for problem: ', terms)
    probDict = dict(zip(fieldKey, terms))
    return probDict

# Testing as you go.
if __name__ == '__main__':
    # self-test code
    probList1=["32 + 698", "3801 + 2", "45 + 43", "123 + 123"]
    for prob in probList1:
        print(separate(prob))
